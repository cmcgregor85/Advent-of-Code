import numpy as np
path = "C:/Users/cmcgregor/source/repos/AdventOfCode/Advent-of-Code/Day8/Day8_Input1.txt"
input = '25512'
storedPosition = 0
storedValue = 0
value = 0
position = 0
numTrees = 0
visibleTrees = set()
row = 1
storedTree = ""
with open(path) as inputFile:
    input = inputFile.read().splitlines()
print(input)
for i in input:
    while storedPosition<len(i):
        storedValue = int(i[storedPosition])
        while position<=storedPosition:
            if position == storedPosition:
                storedTree = str(row)+'-'+str(storedPosition)
                visibleTrees.add(storedTree)
            value=int(i[position])
            if value>=storedValue:
                break
            position+=1
        position = storedPosition
        
        while position<len(i):
            if position == (len(i)-1):
                storedTree = str(row)+'-'+str(storedPosition)
                visibleTrees.add(storedTree)  
                break          
            value=int(i[position+1])
            if value>=storedValue:
                break
            position+=1

        storedPosition+=1
        position = 0
    storedPosition = 0
    position = 0
    row+=1
#input = np.rot90(input,1)
#print(input)
print(visibleTrees)
for x in visibleTrees:
    numTrees+=1
print(numTrees)



