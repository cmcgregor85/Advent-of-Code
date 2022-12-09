input = '30373'
storedPosition = 0
storedValue = 0
value = 0
position = 0
numTrees = 0
while storedPosition<len(input):
    storedValue = input[storedPosition]
    while position<=storedPosition:
        if position == storedPosition:
            numTrees+=1
            break
        value=input[position]
        if value>=storedValue:
            break
        position+=1
    position = 0
    storedPosition+=1
print(numTrees)



