
import pickle
import zmq

class LevelDBClient(object):

    def __init__(self, host, port):
        self.context = context = zmq.Context()
        self.socket = context.socket(zmq.REQ)
        self.socket.connect('tcp://{}:{}'.format(host, port))
    
    def _execute(self, method, key, value=None, sync=False):
        # value is default for .get
        p = (method, key, value, sync)
        self.socket.send(pickle.dumps(p))
        received = self.socket.recv()
        r = pickle.loads(received)
        error, data = r
        if error:
            raise Exception(error)
        return data
    
    def _check(self, k):
        # if isinstance(k, bytes):
        #     return k
        return pickle.dumps(k)
    
    def put(self, k, v, sync=False):
        k = self._check(k)
        v = self._check(v)
        return self._execute('put', k, v, sync=sync)
    
    def get(self, k, default=None):
        k = self._check(k)
        v = self._execute('get', k, value=default)
        try:
            v = pickle.loads(v)
        except:
            pass
        return v
    
    def delete(self, k, sync=False):
        k = self._check(k)
        return self._execute('delete', k, sync=sync)
    
    def put_batch(self, values):
        values_valid = [
            (self._check(k), self._check(v))
            for k, v in values
        ]
        return self._execute('put_batch', values_valid)
