import uuid
from queue import Queue
from queue import Empty
import threading

# lock = threading.Lock()


class SimpleQueue:

    def __init__(self, ack=False):
        self._queue = Queue()
        self._dict = {}
        self._ack = ack

    def put(self, data):
        try:
            # lock.acquire()
            _qid = str(uuid.uuid1())
            self._queue.put((data, _qid))
            self._dict[_qid] = data
            return _qid
        finally:
            # lock.release()
            pass

    def put_batch(self, data_list):
        qid_list = [self.put(_item) for _item in data_list]
        return qid_list

    def get(self, block=False, timeout=None):
        try:
            # lock.acquire()
            _data, _qid = self._queue.get(block=block, timeout=timeout)
            if not self._ack:
                del self._dict[_qid]
            return _data, _qid
        except Empty:
            return None, None
        finally:
            # lock.release()
            pass

    def get_batch(self, block=False, timeout=None, num=1000):
        data_list = []
        try:
            # lock.acquire()
            while len(data_list) < num:
                _data, _qid = self._queue.get(block=block, timeout=timeout)
                if not self._ack:
                    del self._dict[_qid]
                data_list.append((_data, _qid))
        except Empty:
            pass
        finally:
            # lock.release()
            pass
        return data_list

    def ack(self, qid):
        if not self._ack:
            return True
        if qid is None:
            return False
        del self._dict[qid]
        return True

    def queue_size(self):
        return self._queue.qsize()

    def dict_size(self):
        return len(self._dict)

    def clear(self):
        self._queue.queue.clear()
        self._dict.clear()