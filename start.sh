#!/bin/sh

cd /app
exec python -m oms.redis.app
