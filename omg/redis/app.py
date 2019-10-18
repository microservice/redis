# -*- coding: utf-8 -*-
import json
import logging
import os
import signal
import subprocess
import threading
import traceback
from typing import Dict

from flask import Flask, jsonify, make_response, request

import redis

from .RLPopThread import RLPopThread

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)-15s %(name)s %(levelname)s %(message)s')
logger = logging.getLogger('app')


class Handler:
    app = Flask(__name__)

    listeners: Dict[str, RLPopThread] = {}

    r = redis.StrictRedis(
        host=os.getenv('REDIS_HOST', 'localhost'),
        port=int(os.getenv('REDIS_PORT', '6379')),
        password=os.getenv('REDIS_PASSWORD', None),
        db=os.getenv('REDIS_DB', None),
    )

    command_methods = {
        'del': 'delete',
        'rpop': 'pop_generic',
        'lpop': 'pop_generic',
        'brpop': 'pop_generic',
        'blpop': 'pop_generic',
        'rpush': 'push_generic',
        'lpush': 'push_generic'
    }

    def execute(self, command):
        req = request.get_json()
        method = self.command_methods.get(command, command)
        return getattr(self, method)(command, req)

    def ok(self, result=None):
        if result is not None:
            if isinstance(result, bytes):
                result = result.decode('utf-8')
        resp = make_response(json.dumps(result))
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp

    def set(self, command, json_req):
        self.r.set(json_req['key'], json_req['value'])
        return self.ok()

    def get(self, command, json_req):
        val = self.r.get(json_req['key'])
        return self.ok(result=val)

    def push_generic(self, command, json_req):
        """
        Handles LPUSH, RPUSH.
        """
        c = getattr(self.r, command)
        c(json_req['key'], json_req['value'])
        return self.ok()

    def pop_generic(self, command, json_req):
        """
        Handles LPOP, RPOP, BLPOP, BRPOP.
        """
        c = getattr(self.r, command)
        val = c(json_req['key'])
        if val:
            if isinstance(val, tuple):  # True if blocking pop.
                return self.ok(val[1])
            else:
                return self.ok(val)
        else:
            return self.ok()

    def delete(self, command, json_req):
        """
        Pretty command - actual command is del.
        """
        self.r.delete(json_req['key'])
        return self.ok()

    def expire(self, command, json_req):
        self.r.expire(json_req['key'], json_req['seconds'])
        return self.ok()

    def listener(self, action):
        req = request.get_json()
        sub_id = req['id']

        if action == 'remove':
            old_thread = self.listeners.get(sub_id)

            if old_thread is not None:
                old_thread.shutdown = True
                return 'ok\n'

            return 'already_inactive\n'

        assert action == 'add'

        # We only support r/lpop for now.
        assert req['event'] == 'rpop' or req['event'] == 'lpop'

        key = req['data']['key']

        old_thread = self.listeners.get(sub_id)
        if old_thread is not None:
            if old_thread.is_alive():
                return 'already_active\n'

        t = RLPopThread(sub_id, req['event'], self.r, key, req['endpoint'])
        t.start()
        self.listeners[sub_id] = t
        return 'ok\n'

    def health(self):
        return 'OK'


class RedisOnDemand:

    def __init__(self, redis_proc: subprocess.Popen):
        self.redis_proc = redis_proc

    def wait(self):
        self.redis_proc.wait()

        logger.error('Redis has exited!')

        # Print stdout for debug.
        while True:
            line = self.redis_proc.stdout.readline()
            if line != b'':
                logger.info(line.rstrip())
            else:
                break
        # Exit as soon as the redis server crashes.
        # Note: sys.exit() will not work here.
        os.kill(os.getpid(), signal.SIGINT)


def app_error(e):
    logger.warn(traceback.format_exc())
    return jsonify({'message': repr(e)}), 400


if __name__ == '__main__':
    # Do we have creds to connect to? If not, let's spawn a redis server
    # at this point. Why do we spawn it here rather than outside? Because if
    # redis dies, then we can exit this script so that the entire service dies.

    if os.getenv('REDIS_HOST') is None:
        logger.warning('Starting self hosted redis server...')
        p = subprocess.Popen('/usr/bin/redis-server /app/redis.conf',
                             stdout=subprocess.PIPE, shell=True)

        server = RedisOnDemand(p)

        t = threading.Thread(target=server.wait, daemon=True)
        t.start()

    handler = Handler()
    handler.app.add_url_rule('/listener/<string:action>',
                             # action=add/remove.
                             'listener', handler.listener, methods=['post'])
    handler.app.add_url_rule('/<string:command>', 'execute', handler.execute,
                             methods=['post'])

    handler.app.add_url_rule('/health', 'health', handler.health,
                             methods=['get'])
    handler.app.register_error_handler(Exception, app_error)
    handler.app.run(host='0.0.0.0', port=8000)
