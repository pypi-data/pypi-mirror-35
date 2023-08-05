
# LevelDB-Server

With leveldb(plyvel), pyzmq

## Run server with docker

Temporary: cause `--rm`

```sh
sudo docker run -it --rm -p 11300:11300 --name=leveldbs infinityfuture/leveldb-server
```

Data presistance

```sh
sudo docker run -it --rm -p 11300:11300 --volume=/tmp/leveldb:/leveldb --name=leveldbs infinityfuture/leveldb-server
```

## Install client from pip

```sh
pip3 install leveldbs --upgrade
```
