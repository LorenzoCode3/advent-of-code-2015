#advent of code 2015 1st day 1st half

import os
script_dir = os.path.dirname(__file__)
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")
string = f.read()
f.close()

result = string.count('(') - string.count(')')
print(result)