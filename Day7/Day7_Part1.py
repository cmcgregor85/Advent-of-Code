path = "C:/Users/cmcgregor/source/repos/AdventOfCode/Advent-of-Code/Day7/Day7_Input.txt"
directories = {'/':0}
currentDir = '/'
dirHist = []
with open(path) as inputFile:
    input = inputFile.read().splitlines()
    for i in input:
        if 'cd' in i:
            if 'cd ..' in i:
                depth = dirHist.index(currentDir)
                currentDir = dirHist[depth-1]
                updateSize = directories[currentDir]
                updateSize += currentSize
                directories[currentDir] = updateSize
                dirHist.pop()
            else:
                currentDir = i[5:]
                dirHist.append(currentDir)

        elif 'dir' in i:
            directoryName = i[4:]
            directories[directoryName] = 0
        elif '$ ls' in i:
            continue
        else:
            currentSize = directories[currentDir]
            currentSize+=int(i[:i.find(' ')])
            directories[currentDir] = currentSize
total = 0
for z in directories:
    if directories[z] < 100000:
        total+=directories[z]

print(total)



            

        


