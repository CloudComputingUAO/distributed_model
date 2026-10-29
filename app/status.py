import json
from collections import Counter
from connection import connect


def main():
    redis = connect()
    pending = redis.llen("tasks:pending")
    results = [json.loads(value) for value in redis.hvals("tasks:results")]
    print(f"Pending: {pending} | Completed: {len(results)}")
    for worker, count in sorted(Counter(row["worker"] for row in results).items()):
        print(f"{worker}: {count} tasks")
    for result in sorted(results, key=lambda row: row["task_id"]):
        print(f"{result['task_id']}: {result['number']}² = {result['square']}")


if __name__ == "__main__":
    main()
