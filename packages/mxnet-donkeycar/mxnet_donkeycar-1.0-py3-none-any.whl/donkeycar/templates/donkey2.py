# !/usr/bin/env python3
"""
Scripts to drive a donkey 2 car and train a model for it.
Usage:
    manage.py (drive) [--model=<model>] [--js] [--chaos]
    manage.py (train) [--tub=<tub1,tub2,..tubn>]  (--model=<model>) [--base_model=<base_model>] [--no_cache] [--gluon]
Options:
    -h --help        Show this screen.
    --tub TUBPATHS   List of paths to tubs. Comma separated. Use quotes to use wildcards. ie "~/tubs/*"
    --js             Use physical joystick.
    --chaos          Add periodic random steering when manually driving
    --gluon          Run with the gluon NN (if trained)
"""
import os
from docopt import docopt

import donkeycar as dk

#import parts
from donkeycar.parts.camera import PiCamera
from donkeycar.parts.transform import Lambda
from donkeycar.parts.gluon_model import GluonCategorical
from donkeycar.parts.gluon_trainer import GluonTrainer
from donkeycar.parts.gluon_dataset import get_train_val_sets
from donkeycar.parts.keras import KerasCategorical
from donkeycar.parts.actuator import PCA9685, PWMSteering, PWMThrottle
from donkeycar.parts.datastore import TubGroup, TubWriter
from donkeycar.parts.controller import LocalWebController, JoystickController
from donkeycar.parts.clock import Timestamp


def drive(cfg, model_path=None, use_joystick=False, use_chaos=False):
    """
    Construct a working robotic vehicle from many parts.
    Each part runs as a job in the Vehicle loop, calling either
    it's run or run_threaded method depending on the constructor flag `threaded`.
    All parts are updated one after another at the framerate given in
    cfg.DRIVE_LOOP_HZ assuming each part finishes processing in a timely manner.
    Parts may have named outputs and inputs. The framework handles passing named outputs
    to parts requesting the same named input.
    """

    V = dk.vehicle.Vehicle()

    clock = Timestamp()
    V.add(clock, outputs='timestamp')

    cam = PiCamera(resolution=cfg.CAMERA_RESOLUTION)
    V.add(cam, outputs=['cam/image_array'], threaded=True)

    if use_joystick or cfg.USE_JOYSTICK_AS_DEFAULT:
        ctr = JoystickController(max_throttle=cfg.JOYSTICK_MAX_THROTTLE,
                                 steering_scale=cfg.JOYSTICK_STEERING_SCALE,
                                 auto_record_on_throttle=cfg.AUTO_RECORD_ON_THROTTLE)
    else:
        # This web controller will create a web server that is capable
        # of managing steering, throttle, and modes, and more.
        ctr = LocalWebController(use_chaos=use_chaos)

    V.add(ctr,
          inputs=['cam/image_array'],
          outputs=['user/angle', 'user/throttle', 'user/mode', 'recording'],
          threaded=True)

    # See if we should even run the pilot module.
    # This is only needed because the part run_condition only accepts boolean
    def pilot_condition(mode):
        if mode == 'user':
            return False
        else:
            return True

    pilot_condition_part = Lambda(pilot_condition)
    V.add(pilot_condition_part, inputs=['user/mode'],
                                outputs=['run_pilot'])

    # Run the pilot if the mode is not user.
    # If the model_path param is to a folder, assume Gluon parameters
    pilot = GluonCategorical() if os.path.isdir(model_path) else KerasCategorical()
    if model_path:
        pilot.load(model_path)

    V.add(pilot, inputs=['cam/image_array'],
          outputs=['pilot/angle', 'pilot/throttle'],
          run_condition='run_pilot')

    # Choose what inputs should change the car.
    def drive_mode(mode,
                   user_angle, user_throttle,
                   pilot_angle, pilot_throttle):
        if mode == 'user':
            return user_angle, user_throttle

        elif mode == 'local_angle':
            return pilot_angle, user_throttle

        else:
            return pilot_angle, pilot_throttle

    drive_mode_part = Lambda(drive_mode)
    V.add(drive_mode_part,
          inputs=['user/mode', 'user/angle', 'user/throttle',
                  'pilot/angle', 'pilot/throttle'],
          outputs=['angle', 'throttle'])

    steering_controller = PCA9685(cfg.STEERING_CHANNEL)
    steering = PWMSteering(controller=steering_controller,
                           left_pulse=cfg.STEERING_LEFT_PWM,
                           right_pulse=cfg.STEERING_RIGHT_PWM)

    throttle_controller = PCA9685(cfg.THROTTLE_CHANNEL)
    throttle = PWMThrottle(controller=throttle_controller,
                           max_pulse=cfg.THROTTLE_FORWARD_PWM,
                           zero_pulse=cfg.THROTTLE_STOPPED_PWM,
                           min_pulse=cfg.THROTTLE_REVERSE_PWM)

    V.add(steering, inputs=['angle'])
    V.add(throttle, inputs=['throttle'])

    # add tub to save data
    inputs = ['cam/image_array', 'user/angle', 'user/throttle', 'user/mode', 'timestamp']
    types = ['image_array', 'float', 'float', 'str', 'str']

    #multiple tubs
    #th = TubHandler(path=cfg.DATA_PATH)
    #tub = th.new_tub_writer(inputs=inputs, types=types)

    # single tub
    tub = TubWriter(path=cfg.TUB_PATH, inputs=inputs, types=types)
    V.add(tub, inputs=inputs, run_condition='recording')

    # run the vehicle
    V.start(rate_hz=cfg.DRIVE_LOOP_HZ,
            max_loop_count=cfg.MAX_LOOPS)




def train(cfg, tub_names, new_model_path, base_model_path=None, gluon=False):
    """
    use the specified data in tub_names to train an artifical neural network
    saves the output trained model as model_name
    """
    X_keys = ['cam/image_array']
    y_keys = ['user/angle', 'user/throttle']
    
    def train_record_transform(record):
        """ convert categorical steering to linear and apply image augmentations """
        record['user/angle'] = dk.util.data.linear_bin(record['user/angle'])
        # TODO add augmentation that doesn't use opencv
        return record

    def val_record_transform(record):
        """ convert categorical steering to linear """
        record['user/angle'] = dk.util.data.linear_bin(record['user/angle'])
        return record

    new_model_path = os.path.expanduser(new_model_path)

    pilot = GluonCategorical() if gluon else KerasCategorical()
    if base_model_path is not None:
        base_model_path = os.path.expanduser(base_model_path)
        pilot.load(base_model_path)

    print('tub_names', tub_names)
    if not tub_names:
        tub_names = os.path.join(cfg.DATA_PATH, '*')
    tubgroup = TubGroup(tub_names)

    total_records = len(tubgroup.df)
    total_train = int(total_records * cfg.TRAIN_TEST_SPLIT)
    total_val = total_records - total_train
    print('train: %d, validation: %d' % (total_train, total_val))
    steps_per_epoch = total_train // cfg.BATCH_SIZE
    print('steps_per_epoch', steps_per_epoch)
    if gluon:
        del tubgroup
        gluon_trainer = GluonTrainer(pilot)
        train_dataloader, val_dataloader = get_train_val_sets(tub_names, cfg.TRAIN_TEST_SPLIT, cfg.BATCH_SIZE)
        gluon_trainer.train(train_dataloader, val_dataloader, saved_model_path=new_model_path)

    else:
        train_gen, val_gen = tubgroup.get_train_val_gen(X_keys, y_keys,
                                                        train_record_transform=train_record_transform,
                                                        val_record_transform=val_record_transform,
                                                        batch_size=cfg.BATCH_SIZE,
                                                        train_frac=cfg.TRAIN_TEST_SPLIT)

        pilot.train(train_gen,
                 val_gen,
                 saved_model_path=new_model_path,
                 steps=steps_per_epoch,
                 train_split=cfg.TRAIN_TEST_SPLIT)


if __name__ == '__main__':
    args = docopt(__doc__)
    cfg = dk.load_config()

    if args['drive']:
        drive(cfg, model_path=args['--model'], use_joystick=args['--js'], use_chaos=args['--chaos'])

    elif args['train']:
        tub = args['--tub']
        new_model_path = args['--model']
        base_model_path = args['--base_model']
        cache = not args['--no_cache']
        gluon = args['--gluon']
        train(cfg, tub, new_model_path, base_model_path, gluon)
