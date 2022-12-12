path = "C:\\Users\\cmcgregor\\source\\repos\\AdventofCode\\Advent-of-Code\\Day10\\Day10_Input1.txt"
x=1
cycleCount = 0
internalClock = 1
currentRow = []

def drawPixel(cycleCount,x,currentRow):
    if (x-1)<=cycleCount<=(x+1):
            currentRow.append('#')
    else:
            currentRow.append(".")
    if len(currentRow) ==40:
            rowList=' '.join(currentRow)
            print(rowList)
            currentRow = []
    return currentRow

with open(path) as inputFile:
    input = inputFile.read().splitlines()
    for line in input:
        cycleCount+=1
        if line == "noop":
            currentRow=drawPixel(cycleCount,x,currentRow)
        else:
            currentRow=drawPixel(cycleCount,x,currentRow)    
            cycleCount+=1             
            currentRow=drawPixel(cycleCount,x,currentRow)
            x+=int(line[5:])    


    #if cycleCount == printer:
        #print(x*printer)    

