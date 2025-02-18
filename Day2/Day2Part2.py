#advent of code 2015 2nd day 2nd half

import os
script_dir = os.path.dirname(__file__)
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")
string = f.read()
f.close()

presents = string.split("\n")

totalRibbon = 0

for present in presents:
    dimensions = present.split("x")
    dimensions = [int(string) for string in dimensions]
    dimensions.sort()
    presentRibbon = (dimensions[0]*2) + (dimensions[1]*2)
    bowRibbon = dimensions[0]*dimensions[1]*dimensions[2]
    totalRibbon += (presentRibbon + bowRibbon)

print(totalRibbon)