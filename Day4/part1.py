path = "C:/Users/Collin/Desktop/Advent of Code/Day4/input.txt"
start = 0
end = 0
with open(path) as inputFile:
    input = inputFile.read().splitlines()
    for i in input:
        if i[1]=="-":
            start = i[0]
        else:
             start = i[0,1]
        print(start)