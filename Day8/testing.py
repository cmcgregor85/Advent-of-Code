input = '30373'
storedPosition = 0
storedValue = 0
value = 0
position = 0
numTrees = 0
visible = bool('TRUE')
visibleTrees = set()
while storedPosition<len(input):
    storedValue = input[storedPosition]
    while position<=storedPosition:
        if position == storedPosition:
            numTrees+=1
            visibleTrees.add(storedPosition)
        value=input[position]
        if value>=storedValue:
            break
        position+=1
    position = storedPosition
    
    while position<len(input):
        if position == (len(input)-1):
            numTrees+=1
            visibleTrees.add(storedPosition)
        value=input[position]
        if value>=storedValue:
            break
        position+=1

    storedPosition+=1

print(visibleTrees)



