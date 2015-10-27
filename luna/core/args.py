#coding=utf8

import re
import json
from webargs import (
    ValidationError,
    Arg as BaseArg
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


class Arg(BaseArg):
    def __init__(self, type_=None, default=None, required=False):
        pass

