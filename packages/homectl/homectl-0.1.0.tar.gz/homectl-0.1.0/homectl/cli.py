import argparse
import os
import sys
from functools import partial

from .__version__ import VERSION


global_parser = argparse.ArgumentParser(add_help=False)
global_parser.add_argument(
    '--config',
    help='homectl config file',
    default=os.path.expanduser(
        os.path.join(
            '~',
            '.config',
            'homectl',
            'config.json'
        )
    )
)
global_parser.add_argument(
    '--debug',
    help=argparse.SUPPRESS,
    action='store_true'
)


def simple_command(subparsers, name, args=None, parents=None):
    if parents is None:
        parents = []
    parser = subparsers.add_parser(name, parents=[global_parser] + parents)
    if args is not None:
        for n, opts in args.items():
            if isinstance(n, tuple):
                short, long = n
                parser.add_argument(short, long, **opts)
            else:
                parser.add_argument(n, **opts)


def build_room_parser(subparsers):
    room_parser = subparsers.add_parser('room')
    room_subparsers = room_parser.add_subparsers(dest='command2')
    cmd = partial(simple_command, room_subparsers)

    cmd('list')
    cmd('add', {'name': {}})
    cmd('select', {'name': {'nargs': '?'}})
    cmd('current')
    cmd('delete', {'name': {'nargs': '?'}})


def build_device_parser(subparsers):
    device_parser = subparsers.add_parser('device')
    device_subparsers = device_parser.add_subparsers(dest='command2')
    room_opt = {('-r', '--room'): {}}
    cmd = partial(simple_command, device_subparsers)
    device_opt = {
        ('-t', '--type'): {
            'default': 'on_off',
            'choices': ['on_off']
        },
        ('-s', '--service'): {
            'default': 'ifttt',
            'choices': ['ifttt']
        },
        ('-g', '--groups'): {
            'nargs': '*'
        }
    }

    cmd(
        'set',
        {
            'name': {'nargs': '?'},
            'state': {},
            **room_opt
        }
    )
    cmd('list', room_opt)
    cmd(
        'add',
        {
            'name': {},
            **device_opt,
            **room_opt
        }
    )
    cmd(
        'edit',
        {
            'name': {'nargs': '?'},
            **device_opt,
            **room_opt
        }
    )
    cmd('select', {'name': {}, **room_opt})
    cmd('current')
    cmd('delete', {'name': {'nargs': '?'}, **room_opt})


def build_group_parser(subparsers):
    group_parser = subparsers.add_parser('group')
    group_subparsers = group_parser.add_subparsers(dest='command2')
    cmd = partial(simple_command, group_subparsers)

    cmd('list')
    cmd('devices', {'name': {'nargs': '?'}})
    cmd('select', {'name': {}})
    cmd('set', {'name': {'nargs': '?'}, 'state': {}})


def build_service_parser(subparsers):
    service_parser = subparsers.add_parser('service')
    service_subparsers = service_parser.add_subparsers(dest='command2')
    cmd = partial(simple_command, service_subparsers)

    cmd('help', {'name': {}})
    cmd('list')
    cmd(
        'add',
        {
            'name': {},
            'opts': {
                'nargs': '*',
                'help': 'key:value pairs'
            }
        }
    )
    cmd(
        'edit',
        {
            'name': {},
            'opts': {
                'nargs': '*',
                'help': 'key:value pairs'
            }
        }
    )
    cmd('delete', {'name': {}})


parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    parents=[global_parser]
)
parser.add_argument(
    '--version',
    action='version',
    help='print version information',
    version='%(prog)s {} for Python {}'.format(
        VERSION,
        sys.version.split('\n')[0],
    ),
)

command_subparsers = parser.add_subparsers(dest='command')
build_room_parser(command_subparsers)
build_device_parser(command_subparsers)
build_group_parser(command_subparsers)
build_service_parser(command_subparsers)
