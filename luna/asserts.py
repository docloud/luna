# coding=utf8

import inspect
from flask import request
from pprint import pprint


def hr():
    print("-"*40)


def point(content="", with_request_context=True):
    hr()
    print(content or "Assert Point")
    frame = inspect.currentframe().f_back
    frame_info = inspect.getframeinfo(frame)
    print("File: {}".format(frame_info.filename))
    print("Line: {}".format(frame_info.lineno))
    print("Function: {}".format(frame_info.function))
    hr()
    if with_request_context:
        print("Arguments")
        if request.args:
            pprint(request.args)
        if request.form:
            pprint(request.form)
        if request.json:
            pprint(request.json)
        hr()
