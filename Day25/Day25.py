import os

filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(filepath, 'r') as file:
    line = file.read()

row, column = line.replace('To continue, please consult the code grid in the manual.'
                            '  Enter the code at row ', '').replace(', column ', 
                            ' ').replace('.', '').split()
row, column = int(row), int(column)
print(f"Row: {row}, Column: {column}")

value = 20151125
multiplier = 252533
divider = 33554393

def get_next_value(value, multiplier, divider):
    return (value * multiplier) % divider

def get_position(row, column):
    diagonal = row + column - 1
    total_cells_before = (diagonal - 1) * diagonal // 2
    return total_cells_before + column

position = get_position(row, column)
print(f"Position in the grid: {position}")

for _ in range(position - 1):
    value = get_next_value(value, multiplier, divider)

print(f"Value at row {row}, column {column}: {value}")