#advent of code 2015 1st day 2nd half

import os
script_dir = os.path.dirname(__file__)
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")
string = f.read()
f.close()

floor = 0
for i in range(len(string)):
    if string[i] == '(':
        floor += 1
    elif string[i] == ')':
        floor -= 1

    if floor == -1:
        print(i+1)
        break