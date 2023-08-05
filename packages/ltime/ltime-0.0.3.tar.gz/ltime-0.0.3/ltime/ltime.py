# Insert your code here.
import time
from util import is_timestamp, isstr


class Ltime(object):

    def __init__(self, struct_time):
        self._struct_time = struct_time
        self._format = "%Y-%m-%d %H:%M:%S"

    @property
    def timestamp(self):
        return time.mktime(self._struct_time)

    @property
    def strftime(self):
        return time.strftime(self._format, self._struct_time)

    def __repr__(self):
        return '{}:{}'.format('Ltime', self.strftime)


def get(*args, **kwargs):

    format = kwargs.get('format', "%Y-%m-%d %H:%M:%S")

    arg_count = len(args)
    if arg_count == 0:
        return Ltime(time.localtime())
    if arg_count == 1:
        arg = args[0]

        if arg is None:
            # return self.type.utcnow()
            return Ltime(time.localtime())

        # try (int, float, str(int), str(float)) -> from timestamp.
        if is_timestamp(arg):
            return Ltime(time.localtime(arg))

        # (str) -> parse.
        elif isstr(arg):
            return Ltime(time.strptime(arg, format))

        else:
            raise TypeError(
                'Can\'t parse single argument type of \'{0}\''.format(type(arg)))
    else:
        raise TypeError('')
