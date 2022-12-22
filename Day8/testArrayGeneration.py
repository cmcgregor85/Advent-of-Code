import numpy as np
path = "C:/Users/cmcgregor/source/repos/AdventOfCode/Advent-of-Code/Day8/Day8_Input1.txt"
input = []
storedPosition = 0
storedValue = 0
value = 0
position = 0
numTrees = 0
visibleTrees = set()
row = 1
storedTree = ""
with open(path) as inputFile:
    input = np.genfromtxt(inputFile,dtype = str,delimiter=1)
print(input)
input = np.swapaxes(input,0,1)
print(input)