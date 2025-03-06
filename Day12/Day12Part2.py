import os
import json

def sum_integers(obj):
    total = 0
    if isinstance(obj, int):
        total += obj
    elif isinstance(obj, list):
        for item in obj:
            total += sum_integers(item)
    elif isinstance(obj, dict):
        if 'red' not in obj.values():
            for value in obj.values():
                total += sum_integers(value)
    return total

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    data = json.load(file)

result = sum_integers(data)
print(result)