# -*- coding: utf-8 -*-
import os
import sys
import yaml
import pygelf  # GelfTcpHandler, GelfUdpHandler, GelfTlsHandler, GelfHttpHandler
import logging
import logging.handlers

sys.path.insert(0, '../')
sys.path.insert(0, '.')
# print(sys.path)

CONFIG_PATH_LOOKUP = [os.curdir,
                      os.getenv('SLACK_BANG_CONFIG_PATH', '.'),
                      os.path.join(os.path.expanduser('~'), '.slack_bang'),
                      '/etc/slack_bang',
                      os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'),
                      ]

SLACK_BANG_CONFIG_PATH = None
config = None

for loc in CONFIG_PATH_LOOKUP:
    config_file = os.path.join(loc, 'config.yml')

    if os.path.exists(config_file) and not config:
        try:
            config = yaml.load(open(config_file))
            break

        except IOError:
            pass

if not config:
    raise Exception('Could not find slack_bang config.yml: %s' % CONFIG_PATH_LOOKUP)

app_config = config.get('app')
web_config = config.get('web')
channel_tokens = config.get('tokens')

if channel_tokens is None:
    channel_tokens = dict()

#
# Setup Logging
#
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('slack_bang')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
#handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
logger.addHandler(handler)

handler = logging.handlers.SysLogHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

handler = pygelf.GelfTcpHandler(host='logtarget.svc.dglecom.net', port=12151)
handler.setFormatter(formatter)
logger.addHandler(handler)

slack_bang_logger = logging.LoggerAdapter(logging.getLogger('slack_bang'),
                                          {'application': 'slack_bang'})

slack_bang_logger.debug('Using config: {config_file}'.format(config_file=config_file))
