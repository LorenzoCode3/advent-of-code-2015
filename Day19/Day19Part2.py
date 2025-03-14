import os
import random

def reduce_molecule(molecule, replacements):
    steps = 0
    random.shuffle(replacements)
    while molecule != 'e':
        for replacement, base in replacements:
            if replacement in molecule:
                molecule = molecule.replace(replacement, base, 1)
                steps += 1
                break
        else:
            return None
    return steps

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    lines = file.read().splitlines()

replacements = []
for line in lines:
    if '=>' in line:
        base, replacement = line.split(' => ')
        replacements.append((replacement, base))
medicine = lines[-1]

steps = None
while steps is None:
    steps = reduce_molecule(medicine, replacements)

print(steps)