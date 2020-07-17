# -*- coding: utf-8 -*-

"""
The audiotsm2.base.tsm module provides an abstract class for real-time
audio time-scale modification procedures.
"""

class TSM(object):
    """An abstract class for real-time audio time-scale modification
    procedures.
    """

    def clear(self):
        raise NotImplementedError

    def flush_to(self, writer):
        raise NotImplementedError

    def get_max_output_length(self, input_length):
        raise NotImplementedError

    def read_from(self, reader):
        raise NotImplementedError

    def run(self, reader, writer, flush=True):
        """
        Runs the TSM procedure on the content of reader and writes the output to writer.
        """
        finished = False
        while not (finished and reader.empty):
            self.read_from(reader)
            _, finished = self.write_to(writer)

        if flush:
            finished = False
            while not finished:
                _, finished = self.flush_to(writer)

            self.clear()

    def set_speed(self, speed):
        raise NotImplementedError

    def write_to(self, writer):
        raise NotImplementedError
