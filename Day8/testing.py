input = '30373'
storedPosition = 0
storedValue = 0
value = 0
position = 0
numTrees = 0
visibleTrees = set()
row = 1
storedTree = ""
while storedPosition<len(input):
    storedValue = int(input[storedPosition])
    while position<=storedPosition:
        if position == storedPosition:
            numTrees+=1
            storedTree = str(row)+'-'+str(storedPosition)
            visibleTrees.add(storedTree)
        value=int(input[position])
        if value>=storedValue:
            break
        position+=1
    position = storedPosition
    
    while position<len(input):
        if position == (len(input)-1):
            numTrees+=1
            storedTree = str(row)+'-'+str(storedPosition)
            visibleTrees.add(storedTree)            
        value=int(input[position])
        if value>=storedValue:
            break
        position+=1

    storedPosition+=1
    position = 0

print(visibleTrees)



