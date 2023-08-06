
# LevelDB-Server

[![travis-ci](https://travis-ci.org/infinityfuture/leveldb-server.svg?branch=master)](https://travis-ci.org/infinityfuture/leveldb-server)

With leveldb(plyvel), pyzmq

## Run server with docker

Temporary: cause `--rm`

Expose port `11300`

```sh
sudo docker run -it --rm -p 11300:11300 --name=leveldbs infinityfuture/leveldb-server
```

Data persistent to `/tmp/leveldb`

```sh
sudo docker run -it --rm -p 11300:11300 --volume=/tmp/leveldb:/leveldb --name=leveldbs infinityfuture/leveldb-server
```

Run server persistent to `/tmp/leveldb`

```sh
sudo docker run --restart=always -d -p 11300:11300 --volume=/tmp/leveldb:/leveldb --name=leveldbs infinityfuture/leveldb-server
```

## Install client from pip

```sh
pip3 install leveldbs --upgrade
```

## Usage

```python
from leveldbs import LevelDBClient

c = LevelDBClient('localhost', 11300)

c.put(b'a', b'b')
print(c.get(b'a'))
c.delete(b'a')
print(c.get(b'a'))
```
