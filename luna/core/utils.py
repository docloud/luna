# coding=utf8

import imp
from luna import (
    config,
    LunaException
)


def choice(checker, seq):
    """
    Choice item from a sequence that pass the checker.

    :param seq: a sequence the checker excepted.
    :param checker: checker function, return True or False
    :return: the first item that checker function return True

    Usage:

        choice(lambda x: x % 3 == 0, [1, 2, 3, 4])
        >>> 3
    """
    for item in seq:
        if not callable(checker):
            raise LunaException('checker must be callable.')
        if checker(item):
            return item
    return None