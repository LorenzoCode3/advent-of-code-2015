import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    lines = file.read()

registers = {'a': 1, 'b': 0}  # Dictionary to store register values
counter = 0 # Program instruction counter(line)

def hlf(register):
    return register // 2

def tpl(register):
    return register * 3

def inc(register):
    return register + 1

def jmp(offset, line):
    return line + offset

def jie(register, offset, line):
    return line + offset if register % 2 == 0 else line + 1

def jio(register, offset, line):
    return line + offset if register == 1 else line + 1

line = lines.split('\n')
while counter < len(line):
    instruction = line[counter].replace(',', '').split()
    operation = instruction[0]

    if operation == 'hlf':
        registers[instruction[1]] = hlf(registers[instruction[1]])
        counter += 1
    elif operation == 'tpl':
        registers[instruction[1]] = tpl(registers[instruction[1]])
        counter += 1
    elif operation == 'inc':
        registers[instruction[1]] = inc(registers[instruction[1]])
        counter += 1
    elif operation == 'jmp':
        counter = jmp(int(instruction[1]), counter)
    elif operation == 'jie':
        counter = jie(registers[instruction[1]], int(instruction[2]), counter)
    elif operation == 'jio':
        counter = jio(registers[instruction[1]], int(instruction[2]), counter)

print("register_a: ", registers['a'], " register_b: ", registers['b'])