import os
from contextlib import contextmanager
import json
import logging
from functools import wraps


INDENT_SPACES = 2
logger = logging.getLogger()


@contextmanager
def json_file(path):
    with open(path) as f:
        data = json.load(f)
    yield data
    with open(path, 'w') as f:
        f.write(json.dumps(data, indent=INDENT_SPACES))


def valid_config(func):
    @wraps(func)
    def _dec(self, *args, **kwargs):
        self.__init_if_missing__()
        return func(self, *args, **kwargs)
    return _dec


class Config(object):
    def __init__(self, path):
        self.path = path
        if os.path.isfile(path):
            logging.debug(f'Loading {self.path}')
            with open(path) as f:
                json.load(f)
        else:
            logging.debug(f'{self.path} not found; creating')
            self.__clear__()

    def __clear__(self):
        dir = os.path.dirname(self.path)
        if not os.path.isdir(dir):
            logging.debug(f'Creating directory {dir}')
            os.mkdir(dir)
        logging.debug(f'Initializing config file {self.path}')
        with open(self.path, 'w') as f:
            f.write(json.dumps({}, indent=INDENT_SPACES))
        self.__init_if_missing__

    def __init_if_missing__(self):
        with json_file(self.path) as config:
            for k in ('rooms', 'services'):
                if k not in config:
                    config[k] = {}

    def __validate_type__(self, type):
        if type not in {'on_off'}:
            raise ValueError(f'unsupported type {type}')

    def __validate_service__(self, service):
        f = getattr(self, f'set_{service}_device')
        if not callable(f):
            raise ValueError(f'unknown service {service}')
        return f

    @property
    def current_room(self):
        with json_file(self.path) as config:
            return config.get('current_room', None)

    @current_room.setter
    def current_room(self, value):
        with json_file(self.path) as config:
            config['current_room'] = value

    def or_current_room(self, value, allow_none=False):
        if value is None:
            if self.current_room is None:
                if allow_none:
                    return None
                raise ValueError('room name must be provided')
            return self.current_room
        return value

    @property
    def current_device(self):
        with json_file(self.path) as config:
            return config.get('current_device', None)

    @current_device.setter
    def current_device(self, value):
        with json_file(self.path) as config:
            config['current_device'] = value

    def or_current_device(self, value, allow_none=False):
        if value is None:
            if self.current_device is None:
                if allow_none:
                    return None
                raise ValueError('device name must be provided')
            return self.current_device
        return value

    @property
    def current_group(self):
        with json_file(self.path) as config:
            return config.get('current_group', None)

    @current_group.setter
    def current_group(self, value):
        with json_file(self.path) as config:
            config['current_group'] = value

    def or_current_group(self, value, allow_none=False):
        if value is None:
            if self.current_group is None:
                if allow_none:
                    return None
                raise ValueError('group name must be provided')
            return self.current_group
        return value

    @valid_config
    def list_room(self, *args, **kwargs):
        with json_file(self.path) as config:
            return list(config.get('rooms', {}).keys())

    @valid_config
    def add_room(self, *args, name=None, **kwargs):
        name = self.or_current_room(name)
        with json_file(self.path) as config:
            if name in config['rooms']:
                raise KeyError(f'room {name} already exists!')
            config['rooms'][name] = {
                'devices': {}
            }
        logger.debug(f'Room {name} added')

    @valid_config
    def delete_room(self, *args, name=None, **kwargs):
        name = self.or_current_room(name)
        with json_file(self.path) as config:
            del config['rooms'][name]
        logger.debug(f'Room {name} deleted')

    @valid_config
    def select_room(self, *args, name=None, **kwargs):
        if name is None:
            raise ValueError('room name must be provided')
        if name not in self.list_room():
            raise KeyError(f'unknown room {name}')
        self.current_device = None
        self.current_room = name
        logger.debug(f'Room {name} selected')

    @valid_config
    def list_device(self, *args, room=None, **kwargs):
        room = self.or_current_room(room)
        with json_file(self.path) as config:
            return list(config['rooms'][room].get('devices', {}).keys())

    @valid_config
    def add_device(
        self,
        *args,
        name=None,
        type=None,
        room=None,
        service='ifttt',
        groups=None,
        **kwargs
    ):
        kwargs = dict(kwargs)
        if name is None:
            raise ValueError('device name must be provided')
        if type is None:
            raise ValueError('type must be provided')
        room = self.or_current_room(room)
        service = kwargs.get('service', 'ifttt').lower()
        self.__validate_service__(service)
        with json_file(self.path) as config:
            _room = config['rooms'][room]
            if name in _room['devices']:
                raise KeyError(
                    f'device {room} already exists in room {name}!'
                )
            _room['devices'][name] = {
                'type': type,
                'service': service,
                'groups': kwargs.get('groups', [])
            }
        logger.debug(f'Device {room}:{name} added')

    @valid_config
    def edit_device(
        self,
        *args,
        name=None,
        room=None,
        **kwargs
    ):
        kwargs = dict(kwargs)
        name = self.or_current_device(name)
        room = self.or_current_room(room)
        print(name, room, kwargs)
        with json_file(self.path) as config:
            room_config = config['rooms'][room]
            device = room_config['devices'][name]
            for k in list(device.keys()):
                if k in kwargs:
                    v = kwargs[k]
                    if k == 'service':
                        self.__validate_service__(v)
                    device[k] = v
                    logger.debug(f'Device {room}:{name}.{k} set to {v}')

    @valid_config
    def delete_device(self, *args, name=None, room=None, **kwargs):
        name = self.or_current_device(name)
        room = self.or_current_room(room)
        with json_file(self.path) as config:
            del config['rooms'][room]['devices'][name]
        logger.debug(f'Device {room}{name} deleted')

    @valid_config
    def select_device(self,  *args, name=None, room=None, **kwargs):
        if name is None:
            raise ValueError('device name must be provided')
        room = self.or_current_room(room)
        if name not in self.list_device(room):
            raise KeyError(f'unknown device {room}:{name}')
        self.current_room = room
        self.current_device = name
        logger.debug(f'Device {room}:{name} selected')

    @valid_config
    def set_device(self, *args, name=None, room=None, state=None, **kwargs):
        name = self.or_current_device(name)
        room = self.or_current_room(room)
        if state is None:
            raise ValueError('must provide state to set device')
        if name not in self.list_device(room):
            raise KeyError(f'unknown device {room}:{name}')
        with json_file(self.path) as config:
            device = config['rooms'][room]['devices'][name]
        f = self.__validate_service__(device['service'])
        ret = f(room, name, state)
        logger.debug(f'Device {room}:{name} set to {state}')
        return ret

    @valid_config
    def list_group(self, *args, **kwargs):
        groups = set()
        with json_file(self.path) as config:
            for room_name, room in config['rooms'].items():
                for dev_name, device in room['devices'].items():
                    for group_name in device.get('groups', []):
                        groups.add(group_name)
        return list(groups)

    @valid_config
    def devices_group(self, *args, name=None, **kwargs):
        name = self.or_current_group(name)
        devices = []
        with json_file(self.path) as config:
            for room_name, room in config['rooms'].items():
                for device_name, device in room['devices'].items():
                    if name in device.get('groups', []):
                        devices.append(f'{room_name}:{device_name}')
        return devices

    @valid_config
    def select_group(self, *args, name=None, **kwargs):
        if name is None:
            raise ValueError('group name must be provided')
        if name not in self.list_group():
            raise KeyError(f'unknown group {name}')
        self.current_group = name
        logger.debug(f'Group {name} selected')

    @valid_config
    def set_group(self, *args, name=None, state=None, **kwargs):
        name = self.or_current_group(name)
        if state is None:
            raise ValueError('must provide state to set device group')
        for device_path in self.devices_group(name=name):
            room_name, device_name = device_path.split(':')
            self.set_device(name=device_name, room=room_name, state=state)

    @valid_config
    def help_service(self, *args, name=None, **kwargs):
        if name is None:
            raise ValueError('service name must be provided')
        # print help for service
        f = getattr(self, f'help_{name}_service')
        if not callable(f):
            raise ValueError(f'unknown service {name}')
        help_options = 'Options:\n' + f()
        indent = ''.join([' '] * INDENT_SPACES)
        help_options = help_options.replace('\n', '\n' + indent)
        return help_options

    @valid_config
    def list_service(self, *args, **kwargs):
        with json_file(self.path) as config:
            return list(config.get('services', {}).keys())

    @valid_config
    def add_service(self, *args, name=None, opts=None, **kwargs):
        if name is None:
            raise ValueError('service name must be provided')
        opts = dict(
            tuple(o.split(':', 1))
            for o in (opts or [])
        )
        with json_file(self.path) as config:
            config['services'][name] = opts
        logger.debug(f'Service {name} added')

    @valid_config
    def edit_service(self, *args, name=None, opts=None, **kwargs):
        if name is None:
            raise ValueError('service name must be provided')
        opts = {
            tuple(o.split(':', 1))
            for o in (opts or [])
        }
        with json_file(self.path) as config:
            for k, v in opts.items():
                config['services'][name][k] = v
                logger.debug(f'Service {name}.{k} set to {v}')

    @valid_config
    def delete_service(self, *args, name=None, **kwargs):
        with json_file(self.path) as config:
            del config['services'][name]
        logger.debug(f'Service {name} deleted')

from . import config_ifttt  # NOQA
