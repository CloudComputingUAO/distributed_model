import argparse
import json
import uuid
from connection import connect


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=12)
    args = parser.parse_args()
    if args.count < 1:
        parser.error("--count must be greater than zero")

    redis = connect()
    batch = uuid.uuid4().hex[:8]
    for number in range(1, args.count + 1):
        task = {"id": f"{batch}-{number:03d}", "number": number}
        redis.lpush("tasks:pending", json.dumps(task))
    print(f"Queued {args.count} tasks. Batch: {batch}")


if __name__ == "__main__":
    main()
