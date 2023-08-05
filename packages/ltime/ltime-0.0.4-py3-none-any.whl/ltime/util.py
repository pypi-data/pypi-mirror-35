from __future__ import absolute_import


def is_timestamp(value):
    if type(value) == bool:
        return False
    try:
        float(value)
        return True
    except:
        return False


def isstr(s):
    return isinstance(s, str)
