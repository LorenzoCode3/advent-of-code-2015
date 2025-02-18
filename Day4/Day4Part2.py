#advent of code 2015 4th day 2nd half

import os
import hashlib

def getInputString(relativePath):
    script_dir = os.path.dirname(__file__)
    rel_path = relativePath
    abs_file_path = os.path.join(script_dir, rel_path)
    f = open(abs_file_path, "r")
    string = f.read()
    f.close()
    return string

def generateMd5Hash(key):
    md5 = hashlib.md5()
    md5.update(key.encode('utf-8'))
    return md5.hexdigest()

string = getInputString("input.txt")
number = 0
foundAnswer = False

while(not foundAnswer):
    key = string + str(number)
    hash = generateMd5Hash(key)
    if hash[:6] == "000000":
        print("found:", hash, key, number)
        foundAnswer = True
    number += 1
