path = "C:/Users/cmcgregor/source/repos/AdventOfCode/Advent-of-Code/Day8/Day8_Input1.txt"
trees = {}
counter = 0
xsize = 0
ysize = 0
leftVisibleTrees = []
rightVisibleTrees = []
topVisibleTrees = []
bottomVisibleTrees = []
#make a dictionary of all the trees and their heights?
#with open(path) as inputFile:
#    input = inputFile.read().splitlines()
#    for line in input:
#        xsize = len(line)
#        for tree in line:
#            trees[counter] = tree
#            counter+=1
#ysize = int(counter/xsize)
#for tree in trees:
#    if tree<xsize:
#        topVisibleTrees.append(tree)
#print(topVisibleTrees)

treeCounter = 0
currentTreeHeight = 0
rowCounter = 0
with open(path) as inputFile:
    input = inputFile.read().splitlines()
    for row in input:
        for tree in row:
            currentTreePos = treeCounter
            currentTreeHeight = row[currentTreePos]
            for tree in row[:currentTreePos]:
                if currentTreePos == treeCounter:
                    break
                treeCounter+=1
                if currentTreeHeight>row[tree]:
                    print('...waht')
