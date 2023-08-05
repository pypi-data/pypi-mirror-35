import xmlrpc.client

class LevelDBClient(object):

    def __init__(self, server_addr):
        self.s = xmlrpc.client.ServerProxy(
            server_addr, use_builtin_types=True,
            allow_none=True
        )
    
    def put(self, k, v):
        return self.s.put(k, v)
    
    def get(self, k):
        return self.s.get(k)
    
    def delete(self, k):
        return self.s.delete(k)


