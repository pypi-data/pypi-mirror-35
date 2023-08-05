from threading import Thread, Event
import time
import logging
from contextlib import contextmanager


logger = logging.getLogger()


class TimedDict(dict):
    def __init__(self, ttl: float = 1, purge_interval: float = 0.1, overwrite_action: str = 'keep_last'):
        """
        Initialization of the TimedDict data type.
        :param ttl:                 [T]ime [T]o [L]ive, specifies the amount of time, in seconds, an element will stay in the TimedDict before being purged.
        :param purge_interval:      Specifies an interval, in seconds, for when the purge thread should run.
        :param overwrite_action:    Various behaviors if an overwrite of a key is about to happen: keep_last (normal / allow overwrite),
                                    keep_first (disallow overwrite) and mean (takes the mean of the old and new value).
        """

        super().__init__()
        self.store = dict()
        self.ttl = ttl
        self.overwrite_action = overwrite_action
        self.purge_interval = purge_interval
        self._poison_pill = False
        self._pause = False
        self._pause_event = Event()
        self._pause_activated = Event()
        self._completed_purge = Event()

        t = Thread(target=self.ttl_remove)
        t.start()

    def __setitem__(self, key, value):
        if self.overwrite_action == 'keep_first':
            if key not in self.store:
                # Do NOT overwrite!
                self.store[key] = value
                return

        elif self.overwrite_action == 'mean':
            if key in self.store:
                # Take the mean of the old and new value
                try:
                    self.store[key] = (self.store[key] + value) / 2
                    return

                except Exception as exp:
                    logger.error(exp)

        self.update({key: value})

    def ttl_remove(self):
        while True:
            if self._poison_pill:
                break

            time.sleep(self.purge_interval)
            _now = time.time()
            keys_to_delete = list()

            if self._pause:
                self._pause_activated.set()
                self._pause_event.wait()
                self._pause_event.clear()

            for k in self.keys():
                if k < _now - self.ttl:
                    keys_to_delete.append(k)

            for key in keys_to_delete:
                try:
                    self.pop(key)
                except KeyError:
                    logger.warning('Key ({deleted_key}) does not exist'.format(deleted_key=key))
                    pass

            self._completed_purge.set()

    def pause(self):
        self._pause = True
        self._pause_activated.wait()
        self._pause_activated.clear()

    def resume(self):
        self._pause = False
        self._pause_event.set()
        self._completed_purge.clear()
        self._completed_purge.wait()

    def stop(self):
        self._poison_pill = True

    @contextmanager
    def protect(self):
        self.pause()
        yield self
        self.resume()
