# -*- coding: utf-8 -*-
import json
import os

from flask import Flask, make_response, request

import redis


class Handler:
    app = Flask(__name__)

    r = redis.StrictRedis(
        host=os.getenv('REDIS_HOST', 'localhost'),
        port=int(os.getenv('REDIS_PORT', '6379')),
        password=os.getenv('REDIS_PASSWORD', None),
        db=os.getenv('REDIS_DB', None),
    )

    pretty_commands = {
        'del': 'delete',
        'rpop': 'pop_generic',
        'lpop': 'pop_generic',
        'brpop': 'pop_generic',
        'blpop': 'pop_generic',
        'rpush': 'push_generic',
        'lpush': 'push_generic',
    }

    def execute(self):
        req = request.get_json()
        command = self.pretty_commands.get(req['command'], req['command'])
        return getattr(self, command)(req)

    def ok(self, result=None, null=False):
        res = {'status': 'ok'}

        if result is not None:
            if isinstance(result, bytes):
                result = result.decode('utf-8')

            res['result'] = result
        elif null:
            res['result'] = None

        resp = make_response(json.dumps(res))
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp

    def set(self, json_req):
        self.r.set(json_req['data']['key'], json_req['data']['value'])
        return self.ok()

    def push_generic(self, json_req):
        """
        Handles LPUSH, RPUSH.
        """
        c = getattr(self.r, json_req['command'])
        c(json_req['data']['key'], json_req['data']['value'])
        return self.ok()

    def pop_generic(self, json_req):
        """
        Handles LPOP, RPOP, BLPOP, BRPOP.
        """
        c = getattr(self.r, json_req['command'])
        val = c(json_req['data']['key'])
        if val:
            if isinstance(val, tuple):  # True if blocking pop.
                return self.ok(val[1])
            else:
                return self.ok(val)
        else:
            return self.ok(null=True)

    def delete(self, json_req):
        """
        Pretty command - actual command is del.
        """
        self.r.delete(json_req['data']['key'])
        return self.ok()


if __name__ == '__main__':
    handler = Handler()
    handler.app.add_url_rule('/', 'execute', handler.execute, methods=['post'])
    handler.app.run(host='0.0.0.0', port=8000)
