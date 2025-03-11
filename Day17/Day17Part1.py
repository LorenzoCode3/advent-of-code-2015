import os
from itertools import combinations 

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    lines = file.read()

def find_combinations(array, target_sum):
    result = []
    for combo_length in range(1, len(array) + 1):
        for combo in combinations(array, combo_length):
            if sum(combo) == target_sum:
                result.append(combo)
    return result

eggnog = 150
containers = []

for line in lines.splitlines():
    containers.append(int(line))

combinations_list = find_combinations(containers, eggnog)
print(len(combinations_list))