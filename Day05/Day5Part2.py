#advent of code 2015 5th day 2nd half

import os

def getInputString(relativePath):
    script_dir = os.path.dirname(__file__)
    rel_path = relativePath
    abs_file_path = os.path.join(script_dir, rel_path)
    f = open(abs_file_path, "r")
    string = f.read()
    f.close()
    return string

def repeatedLetter(word):
    for i in range(len(word) - 2):
        if word[i] == word[i+2]:
            return True
    return False

def doublePair(word):
    distance = 2
    for index in range(len(word) - 2):
        for offset in range(2, len(word), 1): #range(start, stop, step)
            if word[index : index + distance] == word[index + offset : index + distance + offset]:
                return True
    return False

string = getInputString("input.txt")
strings = string.split("\n")

niceStrings = 0

for word in strings:
    if repeatedLetter(word):
        if doublePair(word):
            niceStrings += 1

print(niceStrings)
