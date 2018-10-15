# redis for Asyncy
This container should be used for connecting to a hosted Redis server. It does not come bundled with its own Redis server.

#### Example

```coffee
# Storyscript
value = redis set key: 'hello' value: 'world'
value = redis get key: 'hello'
value = redis del key: 'hello'
value = redis lpush key: 'hello' value: 'world1'
value = redis rpush key: 'hello' value: 'world2'
value = redis lpop key: 'hello'
value = redis rpop key: 'hello'
```
