path = "C:/Users/Collin/Desktop/Advent of Code/Day3/input.txt"
firstLine = ""
secondLine = ""
thirdLine = ""
firstCommon = ""
char = ""
total = 0
value = 0
x = 0
characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
with open(path) as inputFile:
    input = inputFile.read().splitlines()
    while x<len(input):
        firstLine = input[0+x]
        secondLine = input[1+x]
        thirdLine = input[2+x]
        for y in firstLine:
            if y in secondLine:
                char = y
                firstCommon+=char
        for z in firstCommon:
            if z in thirdLine:
                char = z
                value = (characters.index(char))+1
                total += value
                firstCommon = ""
                break
        x+=3
    print(total)