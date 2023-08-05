
import pickle
import zmq

class LevelDBClient(object):

    def __init__(self, host, port):
        self.context = context = zmq.Context()
        self.socket = context.socket(zmq.REQ)
        self.socket.connect('tcp://{}:{}'.format(host, port))
    
    def _execute(self, method, key, value=b''):
        p = (method, key, value)
        self.socket.send(pickle.dumps(p))
        r = self.socket.recv()
        error, data = pickle.loads(r)
        if error:
            raise Exception(error)
        return data
    
    def _check(self, k):
        if isinstance(k, bytes):
            return k
        return pickle.dumps(k)
    
    def put(self, k, v):
        k = self._check(k)
        v = self._check(v)
        return self._execute('put', k, v)
    
    def get(self, k):
        k = self._check(k)
        return self._execute('get', k)
    
    def delete(self, k):
        k = self._check(k)
        return self._execute('delete', k)
