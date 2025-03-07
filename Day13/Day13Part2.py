import os
import itertools

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    lines = file.read()

names = set()
happiness = dict()

for line in lines.splitlines():
    (name, _, sign, happ, neighbor) = line.replace('.', '').replace('happiness units by sitting next to ', '').split()
    names.add(name)
    names.add(neighbor)
    happiness.setdefault(name, dict())[neighbor] = -int(happ) if sign == 'lose' else int(happ)

for name in names:
    happiness.setdefault('Me', dict())[name] = 0
    happiness.setdefault(name, dict())['Me'] = 0
names.add('Me')

max_happiness = 0
max_permutation = []

for permutation in itertools.permutations(names):
    total_happiness = 0
    
    for i in range(len(permutation) - 1):
        person = permutation[i]
        person_neighbor = permutation[i + 1]
        total_happiness += happiness[person][person_neighbor]
        total_happiness += happiness[person_neighbor][person]
    total_happiness += happiness[permutation[len(permutation) - 1]][permutation[0]]
    total_happiness += happiness[permutation[0]][permutation[len(permutation) - 1]]

    if total_happiness > max_happiness:
        max_happiness = total_happiness
        max_permutation = permutation

print("Percorso:", " -> ".join(max_permutation))
print("Distanza:", max_happiness)