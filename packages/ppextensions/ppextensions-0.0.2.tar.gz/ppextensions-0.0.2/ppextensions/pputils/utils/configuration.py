"""Configuration management for PPExtensions."""

import json
import os

from ppextensions.pputils.utils import FileSystemReaderWriter
from ppextensions.pputils.utils.constants import HOME_PATH, CONFIG_FILE

PATH = os.path.join(HOME_PATH, CONFIG_FILE)


def load_conf(path, fsrw_class=None):
    """
    Creates a dictionary of configuration by reading from the configuration file.
    """
    if fsrw_class is None:
        fsrw_class = FileSystemReaderWriter

    config_file = fsrw_class(path)
    config_file.ensure_file_exists()
    config_text = config_file.read_lines()
    line = u"".join(config_text).strip()

    if line == u"":
        conf_details = {}
    else:
        conf_details = json.loads(line)
    return conf_details


def conf_info(engine):
    """
    Returns a dictionary of configuration by reading from the configuration file.
    """
    conf_details = load_conf(PATH)
    config_dict = {}

    if engine in conf_details:
        config_dict = conf_details[engine]

    return config_dict
