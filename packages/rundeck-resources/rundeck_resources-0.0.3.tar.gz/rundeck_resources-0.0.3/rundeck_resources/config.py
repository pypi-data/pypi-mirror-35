import configparser
from .common import check_file


def read_config(path: str) -> dict:
    """
    Method to read the init configuration file.
    :param path: The path to the init configuration file.
    :type path: str.
    :returns: The content of the configuration file.
    :rtype: dict.
    """
    config_path = check_file(path)
    config = configparser.ConfigParser()
    config.read(config_path)
    configuration = {}
    for section in config.sections():
        configuration[section] = {}
        for key, val in config.items(section):
            configuration[section][key] = val
    return configuration
