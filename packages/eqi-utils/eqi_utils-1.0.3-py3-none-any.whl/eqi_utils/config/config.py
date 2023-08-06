import configparser
import os
from pathlib import Path

_EQI_CONFIG_HOME = 'EQI_HOME'
_EQI_CONFIG_PROFILE = 'EQI_PROFILE'
DEFAULT_CONFIG_FILENAME = 'config.ini'


def get_eqi_home() -> str:
    """Return the EQI home folder path."""
    default_eqi_home = str(Path.home().joinpath('.eqi'))
    return os.getenv(_EQI_CONFIG_HOME, default_eqi_home)


def _get_config_profile():
    return os.getenv(_EQI_CONFIG_PROFILE, 'default')


def _load_eqi_config():
    config_folder = get_eqi_home()
    config_parser = configparser.ConfigParser()
    config_parser.read(os.path.join(config_folder, DEFAULT_CONFIG_FILENAME))
    return config_parser


def reload_config():
    """Reload EQI config."""
    global EQI_CONFIG
    EQI_CONFIG = EqiConfig()


class EqiConfig:
    def __init__(self):
        eqi_config = _load_eqi_config()
        profile = _get_config_profile()
        if profile not in eqi_config:
            raise Exception('Profile {} is not found'.format(profile))
        self.config = eqi_config[profile]

    def get_optional(self, key, default):
        return self.config.get(key, default)

    def get_mandatory(self, key):
        if key not in self.config:
            raise Exception(
                'Value cannot be found for config key {}, please set '
                'accordingly'.format(key))
        return self.config[key]


EQI_CONFIG = EqiConfig()
