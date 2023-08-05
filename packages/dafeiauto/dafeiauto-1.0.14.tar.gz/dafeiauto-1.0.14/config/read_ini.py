# -*- coding:utf-8 -*-
import configparser, os

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

class OperationalError(Exception):
    """operation error."""


class Dictionary(dict):
    """ custom dict."""

    def __getattr__(self, key):
        return self.get(key, None)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

class Read:
    """
    :param file_name 默认是config.ini输入什么文件名就会读xxx.ini
    """
    def __init__(self, file_name='config', cfg=None):
        env = {}
        for key, value in os.environ.items():
            if key.startswith(file_name.upper() + "_"):
                env[key] = value

        ini_config = configparser.ConfigParser(env)

        if cfg:
            ini_config.read(cfg)
        else:
            ini_config.read(os.path.join(CURRENT_PATH, file_name + '.ini'), encoding='UTF-8'), '%s.ini' % file_name

        for section in ini_config.sections():
            setattr(self, section, Dictionary())
            for name, raw_value in ini_config.items(section):
                try:
                    if ini_config.get(section, name) in ['0', '1']:
                        raise ValueError

                    value = ini_config.getboolean(section, name)
                except ValueError:
                    try:
                        value = ini_config.getint(section, name)
                    except ValueError:
                        value = ini_config.get(section, name)
                setattr(getattr(self, section), name, value)

    def get(self, section):
        try:
            return getattr(self, section)
        except AttributeError as e:
            raise OperationalError("Option %s is not found in "
                                         "configuration, error: %s" %
                                         (section, e))

