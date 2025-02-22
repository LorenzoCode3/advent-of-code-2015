#advent of code 2015 7th day 1st half

import operator
import os
import numpy

def getInputString(relativePath):
    with open(os.path.join(os.path.dirname(__file__), relativePath), "r") as file:
        return file.read()

def getValue(item):
    try:
        return numpy.uint16(item)
    except ValueError:
        return numpy.uint16(outputs[item])

def doInstruction(instruction):
    if len(instruction) == 1:
        return getValue(instruction[0])
    if len(instruction) == 2:
        return operations[instruction[0]](getValue(instruction[1]))
    in1 = getValue(instruction[0])
    op = instruction[1]
    in2 = getValue(instruction[2])
    return operations[op](in1, in2)

instructions = getInputString("input.txt")

inputs = {}
for instruction in instructions.splitlines():
    ops, wire = instruction.split(" -> ")
    inputs[wire] = ops.split()

outputs = {}
operations = {
    "AND": operator.and_,
    "OR": operator.or_,
    "LSHIFT": operator.lshift,
    "RSHIFT": operator.rshift,
    "NOT": lambda x: ~x
}

while inputs:
    for key, instruction in list(inputs.items()):
        try:
            outputs[key] = doInstruction(instruction)
            del inputs[key]
        except KeyError:
            continue

print("Wire a:", outputs["a"])
