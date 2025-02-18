#advent of code 2015 6th day 2nd half

import os
import numpy

def getInputString(relativePath):
    script_dir = os.path.dirname(__file__)
    rel_path = relativePath
    abs_file_path = os.path.join(script_dir, rel_path)
    f = open(abs_file_path, "r")
    string = f.read()
    f.close()
    return string

def controlLights(action, startingCoord, endingCoord):
    #dividere starting/ending coord
    startingCoord = startingCoord.split(",")
    endingCoord = endingCoord.split(",")
    startingCoord = list(map(int, startingCoord))
    endingCoord = list(map(int, endingCoord))
    print(startingCoord, endingCoord, action)
    if action == "turnOn":
        for i in range(startingCoord[0], endingCoord[0] + 1):
            for j in range(startingCoord[1], endingCoord[1] + 1):
                matrix[i][j] += 1
    elif action == "turnOff":
        for i in range(startingCoord[0], endingCoord[0] + 1):
            for j in range(startingCoord[1], endingCoord[1] + 1):
                if matrix[i][j] > 0:
                    matrix[i][j] -= 1
    elif action == "toggle":
        for i in range(startingCoord[0], endingCoord[0] + 1):
            for j in range(startingCoord[1], endingCoord[1] + 1):
                matrix[i][j] += 2

string = getInputString("input.txt")
strings = string.split("\n")

matrix = numpy.zeros((1000,1000), int)

for line in strings:
    instruction = line.split()
    if instruction[0] == "turn":
        if instruction[1] == "on":
            controlLights("turnOn", instruction[2], instruction[4])
        elif instruction[1] == "off":
            controlLights("turnOff", instruction[2], instruction[4])
    elif instruction[0] == "toggle":
        controlLights("toggle", instruction[1], instruction[3])

totalBrightness = 0

rows = matrix.shape[0]
cols = matrix.shape[1]

for i in range(0, rows):
    for j in range(0, cols):
        totalBrightness += matrix[i][j]

print(totalBrightness)