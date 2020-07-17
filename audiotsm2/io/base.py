# -*- coding: utf-8 -*-

class Reader(object):
    @property
    def channels(self):
        raise NotImplementedError()

    @property
    def empty(self):
        raise NotImplementedError()


class Writer(object):
    @property
    def channels(self):
        raise NotImplementedError()