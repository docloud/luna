#coding=utf8

"""
A wrapper for webargs library. parse arguments from http requests.
"""

import re
import json
from webargs import (
    ValidationError,
    Arg as BaseArg,
    Missing
)

" Regular Expression "

EMAIL_PATTERN = re.compile(r'.+@[\w\W]+\.')

" Argument types "

class Json(dict):
    def __init__(self, s):
        super(dict, self).__init__()
        data = json.loads(s)
        for key in data:
            self[key] = data[key]

    def __str__(self):
        return json.dumps(self)

" Argument Validators "

class Email(str):
    def __init__(self, email):
        super(str, self).__init__(email)

    @classmethod
    def validator(cls, email):
        if not EMAIL_PATTERN.match(email):
            raise ValidationError('Email is invalid.')
        return email


class Arg(BaseArg):
    def __init__(self, type_=None, default=None, required=False):
        pass

    def validated(self, name, value):
        if value is Missing:
            return value
        if self.multiple and isinstance(value, (list, tuple)):
            return [self._validate(name, each) for each in value]
        else:
            return self._validate(name, value)

        validator = getattr(self.type, 'validator', None)
        if validator:
            value = validator(value)

        super(Arg, self).validated(name=name, value=value)