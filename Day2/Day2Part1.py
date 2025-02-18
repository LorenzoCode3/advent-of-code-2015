#advent of code 2015 2nd day 1st half

import os
script_dir = os.path.dirname(__file__)
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, "r")
string = f.read()
f.close()

presents = string.split("\n")

totalWrappingPaper = 0

for present in presents:
    dimensions = present.split("x")
    dimensions = [int(string) for string in dimensions]
    l = dimensions[0]
    w = dimensions[1]
    h = dimensions[2]
    presentArea = (2*l*w) + (2*w*h) + (2*h*l)
    dimensions.sort()
    extraArea = dimensions[0]*dimensions[1]
    totalWrappingPaper += (presentArea + extraArea) 

print(totalWrappingPaper)