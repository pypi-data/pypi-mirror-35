import xmlrpc.client

class LevelDBClient(object):

    def __init__(self, server_addr):
        self.s = xmlrpc.client.ServerProxy(
            server_addr, use_builtin_types=True,
            allow_none=True
        )
    
    def _check(self, k):
        assert isinstance(k, (bytes, str)), 'Need be bytes or str'
        if isinstance(k, str):
            k = k.encode('utf-8')
        return k
    
    def put(self, k, v):
        k = self._check(k)
        v = self._check(v)
        return self.s.put(k, v)
    
    def get(self, k):
        k = self._check(k)
        return self.s.get(k)
    
    def delete(self, k):
        k = self._check(k)
        return self.s.delete(k)
