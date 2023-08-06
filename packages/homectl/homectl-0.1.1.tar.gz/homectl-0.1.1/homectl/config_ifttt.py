import logging
from . import config
import pyfttt
logger = logging.getLogger()


class IFTTTConfig(config.Config):
    def set_ifttt_device(self, room, device, state):
        with config.json_file(self.path) as cfg:
            service_config = cfg['services']['ifttt']
            room_config = cfg['rooms'][room]
        device_config = room_config['devices'][device]
        device_type = device_config['type']
        values = {}
        if device_type == 'on_off':
            event = f'{room}_{device}_{state}'.lower()
            state = state.lower()
            if state not in ('on', 'off'):
                raise ValueError(
                    f'Invalid state {state} for '
                    f'device of type {device_type}'
                )
        pyfttt.send_event(
            service_config['key'],
            event,
            **values
        )
        logger.debug(f'IFTTT event {event} triggered')

    def help_ifttt_service(self):
        # print IFTTT configuration help
        return 'key: <IFTTT_KEY>'


setattr(config, 'Config', IFTTTConfig)
logger.debug('IFTTT plugin loaded')
