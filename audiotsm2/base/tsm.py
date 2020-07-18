'''base/tsm.py'''

"""
The audiotsm2.base.tsm module provides an abstract class for real-time
audio time-scale modification procedures.
"""

class TSM(object):
    """An abstract class for real-time audio time-scale modification
    procedures.
    """

    def run(self, reader, writer, flush=True):
        finished = False
        while not (finished and reader.empty):
            self.read_from(reader)
            _, finished = self.write_to(writer)

        if flush:
            finished = False
            while not finished:
                _, finished = self.flush_to(writer)

            self.clear()