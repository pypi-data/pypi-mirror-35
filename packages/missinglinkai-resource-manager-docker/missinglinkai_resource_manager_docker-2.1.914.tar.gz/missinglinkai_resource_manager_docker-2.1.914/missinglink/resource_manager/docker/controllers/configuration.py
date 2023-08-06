import logging
import os
import socket

import yaml

WS_SERVER = os.environ.get('WS_SERVER') or 'localhost:8765'
logger = logging.getLogger(__name__)


class ConfigurationError(Exception):
    pass


class ConfigFile(object):
    @classmethod
    def load_yaml_file(cls, path):
        if os.path.isfile(path):
            with open(path) as f:
                return yaml.load(f) or {}
        return {}

    @classmethod
    def save_yaml_file(cls, path, data):
        with open(path, 'w') as f:
            yaml.safe_dump(data, f, default_flow_style=False)

    def __init__(self, path, default_config=None):
        super(ConfigFile, self).__setattr__('path', path)
        super(ConfigFile, self).__setattr__('default_config', default_config or {})
        super(ConfigFile, self).__setattr__('data', self.load_yaml_file(path))

    def __getattr__(self, item):
        if item in self.data:
            return self.data[item]

        return self.default_config[item]

    def __setattr__(self, key, value):
        self.data[key] = value

    def get(self, item, default=None):
        return self.data.get(item, self.default_config.get(item, default))

    def save(self):
        self.save_yaml_file(self.path, self.data)


class ConfigurationInstance(object):
    @classmethod
    def get_default_configuration(cls):
        return {
            'general': {
                'backend_base_url': 'https://missinglink-staging.appspot.com',
                'env': {},
                'hostname': socket.gethostname(),
                'mount': {},
                'ws_server': 'ws://rm-ws-prod.missinglink.ai',
                'pull_job': None,
                'git_image': 'missinglinkai/git-lfs:latest',
                'shell_image': 'library/bash:latest',
                'missinglink_image': 'missinglinkai/missinglink:latest',
                'config_volume': os.environ.get('ML_CONFIG_VOLUME', 'ml_config_volume')
            }
        }

    def __init__(self, config_path=None):
        config_path = config_path or './config'
        logger.info('Configuration path is %s', config_path)
        os.makedirs(config_path, exist_ok=True)
        self.config_path = config_path
        self.general = ConfigFile(os.path.join(config_path, 'index.yaml'), self.get_default_configuration()['general'])


active_config = None


def get_active_config():
    return active_config
