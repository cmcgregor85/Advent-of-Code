path = "C:/Users/cmcgregor/source/repos/AdventOfCode/Advent-of-Code/Day6/Day6_input.txt"
with open(path) as inputFile:
    input = inputFile.read()
    counter = 0
    windowSet = set()
    windowLen = 4
    while counter<len(input):
        window = input[(0+counter):(windowLen+counter)]
        for x in window:
            windowSet.add(x)
        counter+=1
        if len(windowSet) == windowLen:
            print(windowSet)
            print(counter+windowLen-1)
            break
        else:
            windowSet.clear()