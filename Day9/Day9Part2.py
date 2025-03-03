import os
import itertools

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    lines = file.read()

places = set()
distances = dict()

for line in lines.splitlines():
    (from_city, _, to_city, _, distance) = line.split()
    places.add(from_city)
    places.add(to_city)
    distances.setdefault(from_city, dict())[to_city] = int(distance)
    distances.setdefault(to_city, dict())[from_city] = int(distance)

max_distance = 0
max_path = None

for permutation in itertools.permutations(places):
    total_distance = 0
    
    for i in range(len(permutation) - 1):
        current_city = permutation[i]
        next_city = permutation[i + 1]
        total_distance += distances[current_city][next_city]

    if total_distance > max_distance:
        max_distance = total_distance
        max_path = permutation

print("Percorso:", " -> ".join(max_path))
print("Distanza:", max_distance)