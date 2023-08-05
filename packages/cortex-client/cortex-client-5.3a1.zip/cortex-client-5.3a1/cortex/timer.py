import time


class Timer:

    def __init__(self):
        self.start_time = None
        self._start_clock = None
        self.end_time = None
        self._end_clock = None
        self.interval = None

    def start(self):
        self._start_clock = time.clock()
        self.start_time = time.time()

    def stop(self):
        self._end_clock = time.clock()
        self.end_time = time.time()
        self.interval = self._end_clock - self._start_clock

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()
