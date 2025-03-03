#advent of code 2015 8th day 2nd half

import os

def getInputString(relativePath):
    with open(os.path.join(os.path.dirname(__file__), relativePath), "r") as file:
        return file.read()

strings = getInputString("input.txt").splitlines()
result = 0

for line in strings:
    result += line.count('\\') + line.count('"') + 2

print(result)