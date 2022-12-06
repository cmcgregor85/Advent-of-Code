import re
path = "C:/Users/Collin/Desktop/Advent of Code/Day5/Day5_input.txt"
list1 = ["Q","F","M","R","L","W","C","V"]
list2 = ["D","Q","L"]
list3 = ["P","S","R","G","W","C","N","B"]
list4 = ["L","C","D","H","B","Q","G"]
list5 = ["V","G","L","F","Z","S"]
list6 = ["D","G","N","P"]
list7 = ["D","Z","P","V","F","C","W"]
list8 = ["C","P","D","M","S"]
list9 = ["Z","N","W","T","V","M","P","C"]
startCondition = [list1,list2,list3,list4,list5,list6,list7,list8,list9]
#startCondition = [['Z','N'],['M','C','D'],['P']]
counter = 0 
count2 = 1
with open(path) as inputFile:
    input = inputFile.read().splitlines()
    
    for i in input:
        ints = [int(s) for s in re.findall(r'\b\d+\b',i)]

        numCrates = int(ints[0])
        srcStack = startCondition[(int(ints[1])-1)]
        destStack = startCondition[(int(ints[2])-1)]
        counter = 0
        print("Line #")
        print(count2)
        print(ints)
        print(srcStack)
        print(destStack)
        print(numCrates)
        count2 += 1

        while counter < numCrates:
            print(srcStack)
            mover = srcStack.pop()
            print(mover)
            destStack.append(mover)
            print(destStack) 
            counter+=1
        
    endString = ""
    for x in startCondition:
        endString+=(x[-1])
    print(startCondition)
    print(endString)
            
        



        
