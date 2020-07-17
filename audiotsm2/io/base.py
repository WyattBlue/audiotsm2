# -*- coding: utf-8 -*-

class Reader(object):
    @property
    def channels(self):
        raise NotImplementedError()

    @property
    def empty(self):
        raise NotImplementedError()

    def read(self, buffer):
        raise NotImplementedError()

    def skip(self, n):
        raise NotImplementedError()


class Writer(object):
    @property
    def channels(self):
        raise NotImplementedError()

    def write(self, buffer):
        raise NotImplementedError()
