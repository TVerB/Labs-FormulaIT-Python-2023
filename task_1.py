# TODO решите задачу
import json


def task() -> float:
    input_file = 'input.json'

    with open(input_file, 'r') as file:
        json_data = json.load(file)

    compositions = [item['score'] * item['weight'] for item in json_data]

    return round(sum(compositions), 3)


print(task())
