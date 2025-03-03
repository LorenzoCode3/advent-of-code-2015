#advent of code 2015 3rd day 2nd half

import os

def getInputString(relativePath):
    script_dir = os.path.dirname(__file__)
    rel_path = relativePath
    abs_file_path = os.path.join(script_dir, rel_path)

    f = open(abs_file_path, "r")
    string = f.read()
    f.close()

    return string

def checkIfAlreadyVisited(position):
    for i in range(len(visitedHouses)):
        if ((position[0] == visitedHouses[i][0]) and (position[1] == visitedHouses[i][1])):
            #print("already present!", position, visitedHouses[i], "house number:", i+1)
            return True
    return False

string = getInputString("input.txt")
moves = list(string)

santaPosition = [0, 0] #[x, y] startingLocation
roboSantaPosition = [0, 0]
visitedHouses = [[0, 0]]
index = 0

for move in moves:
    if (index % 2) == 0: #santa turn
        if move == ">":
            santaPosition[0] += 1
        elif move == "v":
            santaPosition[1] -= 1
        elif move == "<":
            santaPosition[0] -= 1
        elif move == "^":
            santaPosition[1] += 1
        if not checkIfAlreadyVisited(santaPosition):
            visitedHouses.append(list(santaPosition))
    else: #robo-santa turn
        if move == ">":
            roboSantaPosition[0] += 1
        elif move == "v":
            roboSantaPosition[1] -= 1
        elif move == "<":
            roboSantaPosition[0] -= 1
        elif move == "^":
            roboSantaPosition[1] += 1
        if not checkIfAlreadyVisited(roboSantaPosition):
            visitedHouses.append(list(roboSantaPosition))
    index += 1

print(len(visitedHouses))