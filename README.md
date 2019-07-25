# _Redis_ OMG Microservice

[![Open Microservice Guide](https://img.shields.io/badge/OMG%20Enabled-👍-green.svg?)](https://microservice.guide)

This container should be used for connecting to a hosted Redis server. It does not come bundled with its own Redis server.

## Direct usage in [Storyscript](https://storyscript.io/):

#### Redis Example
```coffee
# Storyscript
value = redis set key: "hello" value: "world"
value = redis get key: "hello"
value = redis del key: "hello"
value = redis lpush key: "hello" value: "world1"
value = redis rpush key: "hello" value: "world2"
value = redis lpop key: "hello"
value = redis rpop key: "hello"

# Streaming example
redis listener as rds
  when rds rpop key: 'foo' as event  # Can also lpop.
    # Do something with event...
```

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMG CLI](https://www.npmjs.com/package/omg)

##### Set
```shell
$ omg run set -a key=<KEY> -a value=<VALUE> -e REDIS_HOST=<REDIS_HOST> -e REDIS_PORT=<REDIS_PORT> -e REDIS_DB=<REDIS_DB> -e REDIS_PASSWORD=<REDIS_PASSWORD>
```
##### RPush
```shell
$ omg run rpush -a key=<KEY> -a value=<VALUE> -e REDIS_HOST=<REDIS_HOST> -e REDIS_PORT=<REDIS_PORT> -e REDIS_DB=<REDIS_DB> -e REDIS_PASSWORD=<REDIS_PASSWORD>
```
##### LPush
```shell
$ omg run lpush -a key=<KEY> -a value=<VALUE> -e REDIS_HOST=<REDIS_HOST> -e REDIS_PORT=<REDIS_PORT> -e REDIS_DB=<REDIS_DB> -e REDIS_PASSWORD=<REDIS_PASSWORD>
```
##### RPop
```shell
$ omg run rpop -a key=<KEY> -e REDIS_HOST=<REDIS_HOST> -e REDIS_PORT=<REDIS_PORT> -e REDIS_DB=<REDIS_DB> -e REDIS_PASSWORD=<REDIS_PASSWORD>
```
##### LPop
```shell
$ omg run lpop -a key=<KEY> -e REDIS_HOST=<REDIS_HOST> -e REDIS_PORT=<REDIS_PORT> -e REDIS_DB=<REDIS_DB> -e REDIS_PASSWORD=<REDIS_PASSWORD>
```
##### BRPop
```shell
$ omg run brpop -a key=<KEY> -e REDIS_HOST=<REDIS_HOST> -e REDIS_PORT=<REDIS_PORT> -e REDIS_DB=<REDIS_DB> -e REDIS_PASSWORD=<REDIS_PASSWORD>
```
##### BLPop
```shell
$ omg run blpop -a key=<KEY> -e REDIS_HOST=<REDIS_HOST> -e REDIS_PORT=<REDIS_PORT> -e REDIS_DB=<REDIS_DB> -e REDIS_PASSWORD=<REDIS_PASSWORD>
```
##### Delete
```shell
$ omg run del -a key=<KEY> -e REDIS_HOST=<REDIS_HOST> -e REDIS_PORT=<REDIS_PORT> -e REDIS_DB=<REDIS_DB> -e REDIS_PASSWORD=<REDIS_PASSWORD>
```
##### Get
```shell
$ omg run get -a key=<KEY> -e REDIS_HOST=<REDIS_HOST> -e REDIS_PORT=<REDIS_PORT> -e REDIS_DB=<REDIS_DB> -e REDIS_PASSWORD=<REDIS_PASSWORD>
```
##### Expire
```shell
$ omg run expire -a key=<KEY> -a seconds=<SECONDS> -e REDIS_HOST=<REDIS_HOST> -e REDIS_PORT=<REDIS_PORT> -e REDIS_DB=<REDIS_DB> -e REDIS_PASSWORD=<REDIS_PASSWORD>
```
##### Listener RPop
```shell
$ omg subscribe listener rpop -a key=<KEY> -e REDIS_HOST=<REDIS_HOST> -e REDIS_PORT=<REDIS_PORT> -e REDIS_DB=<REDIS_DB> -e REDIS_PASSWORD=<REDIS_PASSWORD>
```
##### Listener LPop
```shell
$ omg subscribe listener lpop -a key=<KEY> -e REDIS_HOST=<REDIS_HOST> -e REDIS_PORT=<REDIS_PORT> -e REDIS_DB=<REDIS_DB> -e REDIS_PASSWORD=<REDIS_PASSWORD>
```
**Note**: The OMG CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/redis/blob/master/LICENSE).


