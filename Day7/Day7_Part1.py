path = "C:\\Users\\Collin\\Source\Advent_Of_Code\\Advent-of-Code\\Day7\\Day7_Input.txt"
directories = {'/':0}
currentDir = ''
dirHist = []
with open(path) as inputFile:
    input = inputFile.read().splitlines()
    for i in input:
        if '$ cd' in i:
            if '$ cd ..' in i:
                depth = dirHist.index(currentDir)
                currentDir = dirHist[depth-1]
                dirHist.pop()
            else:
                currentDir = currentDir + i[5:]
                dirHist.append(currentDir)

        elif 'dir' in i:
            directoryName = currentDir + (i[4:])
            directories[directoryName] = 0
        elif '$ ls' in i:
            continue
        else:
            for x in dirHist:
                currentSize = directories[x]
                currentSize+=int(i[:i.find(' ')])
                directories[x] = currentSize
total = 0
for z in directories:
    if directories[z] < 100000:
        total+=directories[z]

print(total)



            

        


