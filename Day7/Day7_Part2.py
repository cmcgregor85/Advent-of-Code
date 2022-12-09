path = "C:\\Users\\Collin\\Source\Advent_Of_Code\\Advent-of-Code\\Day7\\Day7_Input.txt"
directories = {'/':0}
currentDir = ''
dirHist = []
directoryList = {}
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
total = 70000000-directories['/']
total = 30000000-total

for z in directories:
    if directories[z] > total:
        directoryList[z]=directories[z]
x=[]
for y in directoryList:
    x.append(directoryList[y])
x.sort()
print(x[0])




            

        


