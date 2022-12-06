path = "C:/Users/Collin/Desktop/Advent of Code/Day3/input.txt"
firstHalf = ""
secondHalf = ""
char = ""
total = 0
value = 0
characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
with open(path) as inputFile:
    input = inputFile.read().splitlines()
    for i in input:
        length = int(len(i)/2)
        firstHalf = i[:length] 
        secondHalf = i[length:]
        for x in firstHalf:
            if x in secondHalf:
                char = x
                print(char)
                value = (characters.index(char))+1
                print(value)
                total += value
                break
    print(total)

            




    