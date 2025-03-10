import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    lines = file.read()

def matches_condition(candidate_value, condition):
    if isinstance(condition, tuple):
        op, num = condition
        if op == '>':
            return candidate_value > num
        elif op == '<':
            return candidate_value < num
        else:
            raise ValueError("Unknown operator: " + op)
    else:
        return candidate_value == condition

aunts = dict()
sue = {
    'children': 3,
    'cats': ('>', 7),
    'samoyeds': 2,
    'pomeranians': ('<', 3),
    'akitas': 0,
    'vizslas': 0,
    'goldfish': ('<', 5),
    'trees': ('>', 3),
    'cars': 2,
    'perfumes': 1
}

for line in lines.splitlines():
    line = line.replace('Sue ', '').replace(',', '').replace(':', '')
    (number, name_field_1, field_1, name_field_2, field_2, name_field_3, field_3) = line.split()
    number, field_1, field_2, field_3 = map(int, (number, field_1, field_2, field_3))
    aunts.setdefault(number, dict({name_field_1: field_1, name_field_2: field_2, name_field_3: field_3}))

matches = {
    key: value
    for key, value in aunts.items()
    if all(matches_condition(value[k], condition) for k, condition in sue.items() if k in value)
}

print("Matches found:")
print(matches)