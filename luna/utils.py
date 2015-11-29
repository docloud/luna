# coding=utf8

"""
Copyright 2015 Luna Project
"""


from pprint import pprint


def hr(n=40, sep='=', log_func=None):
    if log_func is None:
        print(n * sep)
    else:
        log_func(n * sep)


def console_log(obj):
    hr()
    pprint(obj)
    hr()