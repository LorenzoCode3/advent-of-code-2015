#advent of code 2015 5th day 1st half

import os

def getInputString(relativePath):
    script_dir = os.path.dirname(__file__)
    rel_path = relativePath
    abs_file_path = os.path.join(script_dir, rel_path)
    f = open(abs_file_path, "r")
    string = f.read()
    f.close()
    return string

def doubleLetter(word):
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            return True
    return False

def vowelsCount(word):
    vowels = 0
    for char in word:
        if char in vowelsMatches:
            vowels += 1
    return vowels

string = getInputString("input.txt")
strings = string.split("\n")

vowelsMatches = ["a", "e", "i", "o", "u"]
avoidMatches = ["ab", "cd", "pq", "xy"]

niceStrings = 0

for word in strings:
    if not any(x in word for x in avoidMatches):
        if vowelsCount(word) >= 3:
            if doubleLetter(word):
                niceStrings += 1

print(niceStrings)