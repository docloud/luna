# coding=utf8

"""
Copyright 2015 Luna Project

A wrapper for webargs library. parse arguments from http requests.
"""

import re
import json
from webargs import (
    ValidationError,
    Arg,
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
