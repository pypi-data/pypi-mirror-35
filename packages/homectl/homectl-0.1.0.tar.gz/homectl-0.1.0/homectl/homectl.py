#!/usr/bin/env python
from . import cli
from .config import Config
import logging


logger = logging.getLogger()


def main(args=None):
    opts = cli.parser.parse_args(args)
    if opts.debug:
        logger.setLevel('DEBUG')
    config = Config(opts.config)
    func_name = '{}_{}'.format(opts.command2, opts.command)
    attr = getattr(config, func_name)
    if isinstance(attr, str):
        print(attr)
    elif isinstance(attr, list):
        for a in attr:
            print(a)
    elif callable(attr):
        ret = attr(**opts.__dict__)
        if isinstance(ret, str):
            print(ret)
        elif isinstance(ret, list):
            for r in ret:
                print(r)
        else:
            return ret
    return 0
