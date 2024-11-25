# TODO решите задачу
import json

def task() -> float:
    with open("input.json", "r") as file:
        data = json.load(file)
    total_sum:float = 0

    for item in data:
        total_sum += item["score"]*item["weight"]
    return round(total_sum, 3)


print(task())
