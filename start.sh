#!/bin/sh

cd /app
exec python -m omg.redis.app
