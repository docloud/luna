# coding=utf8

import os
import inspect
from flask import request
from pprint import pprint
from .utils import console_log


def point(content="", with_request_context=True):
    frame = inspect.currentframe().f_back
    frame_info = inspect.getframeinfo(frame)
    log = os.linesep.join([
        content or "Assert Point",
        "File: {}".format(frame_info.filename),
        "Line: {}".format(frame_info.lineno),
        "Function: {}".format(frame_info.function)
    ])
    console_log(log)
    if with_request_context:
        print("Arguments")
        if request.args:
            pprint(request.args)
        if request.form:
            pprint(request.form)
        if request.json:
            pprint(request.json)
