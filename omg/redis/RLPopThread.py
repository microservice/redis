# -*- coding: utf-8 -*-
import datetime
import requests
import traceback
import uuid
from redis import StrictRedis

from threading import Thread


class RLPopThread(Thread):
    shutdown = False

    def __init__(self, sub_id: str, command: str, redis: StrictRedis,
                 queue_name: str, endpoint: str) -> None:
        super().__init__(name=sub_id, daemon=True)
        self.redis = redis
        assert command == 'rpop' or command == 'lpop'
        self.command = command
        self.queue_name = queue_name
        self.endpoint = endpoint

    def run(self) -> None:
        while True:
            # The following is equivalent to a = self.redis.brpop()
            val = getattr(self.redis, f'b{self.command}')(self.queue_name,
                                                          timeout=5)
            if self.shutdown:
                return

            if val is None:
                continue

            val = val[1].decode('utf-8')

            # Make a POST req to the endpoint
            tries = 0
            event_id = str(uuid.uuid4())
            while tries <= 3:
                tries += 1
                try:
                    res = requests.post(url=self.endpoint, json={
                        'cloudEventsVersion': '0.1',
                        'eventType': 'redis',
                        'source': '/listener/add',
                        'eventID': event_id,
                        'eventTime': datetime.datetime.now().isoformat(),
                        'data': val
                    })
                    if int(res.status_code / 100) == 2:
                        break
                except:
                    # Eat blindly.
                    traceback.print_exc()
                    pass
