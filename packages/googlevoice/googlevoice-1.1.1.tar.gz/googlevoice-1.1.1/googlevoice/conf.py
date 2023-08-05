import os

import six
from six.moves import configparser

from . import settings


class Config(configparser.ConfigParser):
    """
    ``ConfigParser`` subclass that looks into your home folder for a file named
    ``.gvoice`` and parses configuration data from it.
    """
    def __init__(self):
        self.fname = os.path.expanduser('~/.gvoice')

        if not os.path.exists(self.fname):
            try:
                f = open(self.fname, 'w')
            except IOError:
                return
            f.write(settings.DEFAULT_CONFIG)
            f.close()

        (
            super(Config).__init__()
            if six.PY3 else
            configparser.ConfigParser.__init__(self)
        )
        try:
            self.read([self.fname])
        except IOError:
            return

    def get(self, option, section='gvoice'):
        try:
            return (
                super(Config, self).get(section, option)
                if six.PY3 else
                configparser.ConfigParser.get(self, section, option).strip()
            ) or None
        except configparser.NoOptionError:
            return

    def set(self, option, value, section='gvoice'):
        return (
            super(Config, self).set(section, option, value)
            if six.PY3 else
            configparser.ConfigParser.set(self, section, option, value)
        )

    def phoneType(self):
        try:
            return int(self.get('phoneType'))
        except TypeError:
            return

    def save(self):
        f = open(self.fname, 'w')
        self.write(f)
        f.close()

    phoneType = property(phoneType)
    forwardingNumber = property(lambda self: self.get('forwardingNumber'))
    email = property(lambda self: self.get('email','auth'))
    password = property(lambda self: self.get('password','auth'))
    secret = property(lambda self: self.get('secret'))

config = Config()
