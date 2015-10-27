# coding=utf8

"""
Configure class for any config file.
"""

import os
import errno
from flask.config import Config as FlaskConfig


class Config(FlaskConfig):
    def from_yaml(self, filename):
        filename = os.path.join(self.root_path, filename)
        try:
            with open(filename) as config_file:
                pass
        except IOError as e:
            if e.errno in (errno.ENOENT, errno.EISDIR):
                return False
            e.strerror = 'Unable to load configuration file (%s)' % e.strerror
            raise
        return True

    def from_unix(self, filename):
        pass