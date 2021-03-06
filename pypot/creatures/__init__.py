import sys

from .abstractcreature import AbstractPoppyCreature

module = sys.modules[__name__]


installed_poppy_creatures = {}
# Feel free to make a pull request to add your own creature here
existing_creatures = ['poppy-humanoid', 'poppy-torso', 'poppy-ergo-jr',
                      'poppy-ergo-starter', 'poppy-6dof-right-arm',
                      'poppy-dragster-mini', 'poppy-ergo', 'roboticia-quattro',
                      'roboticia-first', 'roboticia-uno', 'roboticia-drive',
                      'doggy', 'poppy-ergo-pusher', 'mila-slider', 'mila-pusher']

# TODO implement user creating a file on the SD card root that has the name of the robot and on boot the sdcard automatically launches the ZMQ server for that robot

for creature in existing_creatures:
    package = creature.replace('-', '_')
    cls_name = ''.join(x.capitalize() or '_' for x in package.split('_'))

    try:
        cls = getattr(__import__(package), cls_name)
        installed_poppy_creatures[creature] = cls
        setattr(module, cls_name, cls)

    except (ImportError, AttributeError):
        pass
