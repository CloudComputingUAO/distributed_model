import json
import os
import socket
import time
from connection import connect


def main():
    redis = connect()
    worker = socket.gethostname()
    duration = float(os.getenv("WORK_SECONDS", "2"))
    print(f"Worker {worker} ready", flush=True)

    while True:
        item = redis.brpop("tasks:pending", timeout=5)
        if item is None:
            continue
        task = json.loads(item[1])
        print(f"Starting {task['id']}", flush=True)
        time.sleep(duration)
        result = {
            "task_id": task["id"],
            "number": task["number"],
            "square": task["number"] ** 2,
            "worker": worker,
        }
        redis.hset("tasks:results", task["id"], json.dumps(result))
        print(f"Finished {task['id']}: {result['square']}", flush=True)


if __name__ == "__main__":
    main()
