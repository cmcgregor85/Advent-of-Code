import numpy as np
path = "C:/Users/cmcgregor/source/repos/AdventOfCode/Advent-of-Code/Day8/Day8_Input.txt"
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
for i in input:
    while storedPosition<len(i):
        storedValue = int(i[storedPosition])
        while position<=storedPosition:
            if position == storedPosition:
                storedTree = str(row)+'-'+str(storedPosition+1)
                visibleTrees.add(storedTree)
            value=int(i[position])
            if value>=storedValue:
                break
            position+=1
        position = storedPosition
        
        while position<len(i):
            if position == (len(i)-1):
                storedTree = str(row)+'-'+str(storedPosition+1)
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

input = np.swapaxes(input,0,1)
row=1
for i in input:
    while storedPosition<len(i):
        storedValue = int(i[storedPosition])
        while position<=storedPosition:
            if position == storedPosition:
                storedTree = str(storedPosition+1)+'-'+str(row)
                visibleTrees.add(storedTree)
            value=int(i[position])
            if value>=storedValue:
                break
            position+=1
        position = storedPosition
        
        while position<len(i):
            if position == (len(i)-1):
                storedTree = str(storedPosition+1)+'-'+str(row)
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

for x in visibleTrees:
    numTrees+=1
print(numTrees)



