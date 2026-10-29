import os
import time
import redis


def connect():
    host = os.getenv("REDIS_HOST", "redis")
    for attempt in range(30):
        try:
            client = redis.Redis(host=host, port=6379, decode_responses=True)
            client.ping()
            return client
        except redis.ConnectionError:
            if attempt == 29:
                raise
            time.sleep(1)
