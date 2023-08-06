import asyncio
import os

from mlcrypto import Asymmetric
from pkg_resources import DistributionNotFound, get_distribution

from missinglink.resource_manager.docker.api import API_MAPPING
from missinglink.resource_manager.docker.controllers.configuration import get_active_config
from missinglink.resource_manager.docker.controllers.transport import Backbone
from .config import init_cluster


class CliTools:
    @classmethod
    def load_config(cls, loop=None):
        conf_path = os.environ.get('MLADMIN_CONF_DIR', os.path.expanduser('~/.config'))
        debug = os.environ.get('MLADMIN_DEBUG') is not None
        loop = loop or asyncio.get_event_loop()
        loop.run_until_complete(init_cluster(config_folder=conf_path))
        return conf_path, debug, loop

    @classmethod
    def is_in_container(cls):
        return os.environ.get("ML_RM_MANAGER") == '1'

    @classmethod
    def populate_ssh_key(cls, active_config, ssh_key_data):
        cipher = Asymmetric.create_from(Asymmetric.ensure_bytes(ssh_key_data))
        active_config.general.default_public_key = cipher.bytes_to_b64str(cipher.export_public_key_bytes())
        active_config.general.default_private_key = cipher.bytes_to_b64str(cipher.export_private_key_bytes('PEM'))
        # todo: load old keys

    @classmethod
    def run_ws(cls, loop=None):
        conf_path, debug, loop = cls.load_config(loop)
        active_config = get_active_config()
        return Backbone.create_and_serve(API_MAPPING, debug, active_config, loop)

    @classmethod
    def get_version(cls, package='missinglinkai-resource-manager-docker'):
        try:
            dist = get_distribution(package)
        except DistributionNotFound:
            return None

        return str(dist.version)

    @classmethod
    def _ensure_b64(cls, config_data_str):
        if 'access_token' in config_data_str:
            return Asymmetric.bytes_to_b64str(config_data_str)

        return config_data_str

    @classmethod
    def save_ml_config(cls, config_prefix, config_data):
        conf_path, debug, loop = cls.load_config()

        ml_path = os.path.join(conf_path, '.MissingLinkAI')
        os.makedirs(ml_path, exist_ok=True)
        filename = 'missinglink.cfg'
        if config_prefix is not None and len(config_prefix) > 0:
            filename = f"{config_prefix}-{filename}"

        config_data = cls._ensure_b64(config_data)
        config = get_active_config()
        config.general.ml_data = config_data
        config.general.ml_path = filename
        get_active_config().general.save()
