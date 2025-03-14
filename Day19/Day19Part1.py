import os
import re

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    lines = file.read()

molecules = []
string = ''

for line in lines.splitlines():
    if '=>' in line:
        base, replacement = line.split(' => ')
        molecules.append((base, replacement))
    elif line:
        string = line

string_parts = re.split(r'(?=[A-Z])', string)[1:]
possibilities = set()

for i, part in enumerate(string_parts):
    for base, replacement in molecules:
        if part == base:
            new_string = string_parts[:i] + [replacement] + string_parts[i+1:]
            possibilities.add(''.join(new_string))

print(len(possibilities))