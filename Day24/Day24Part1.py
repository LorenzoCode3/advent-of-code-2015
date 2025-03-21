from os import path
from functools import reduce
from itertools import combinations
from operator import mul

filepath = path.join(path.dirname(__file__), 'input.txt')
weights = [int(weight) for weight in [line.strip("\n") for line in open(filepath, 'r')]]

def find_min_quantum_entanglement(num_groups):
    group_size = sum(weights) // num_groups
    for i in range(len(weights)):
        quantum_entanglements = [reduce(mul, combination) for combination in combinations(weights, i) 
            if sum(combination) == group_size]
        if quantum_entanglements:
            return min(quantum_entanglements)

print(find_min_quantum_entanglement(3))