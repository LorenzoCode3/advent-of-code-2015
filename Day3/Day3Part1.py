#advent of code 2015 3rd day 1st half

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
visitedHouses = [[0, 0]]
numberOfVisitedHouses = 1 #first house[0, 0] already visited

for move in moves:
    if move == ">":
        santaPosition[0] += 1
    elif move == "v":
        santaPosition[1] -= 1
    elif move == "<":
        santaPosition[0] -= 1
    elif move == "^":
        santaPosition[1] += 1
    
    if not checkIfAlreadyVisited(santaPosition):
        numberOfVisitedHouses += 1
        #print(santaPosition, numberOfVisitedHouses)

    visitedHouses.append(list(santaPosition))

print(numberOfVisitedHouses)