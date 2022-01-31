import time


class TimerError(Exception):
    """A custom exception used to report errors of the Timer class."""


class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Starts a new timer"""
        if self._start_time is not None:
            raise TimerError('Timer is running. Use .stop() to stop it.')

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report elapsed time."""
        if self._start_time is None:
            raise TimerError('Timer is not running. Use .start() to start it.')

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f'Elapsed Time: {elapsed_time:0.4f} seconds')
