path = "C:/Users/cmcgregor/source/repos/AdventOfCode/Advent-of-Code/2015/Day2Input.txt"
with open(path) as inputFile:
    input = inputFile.read().splitlines()
    total = 0
    for i in input:
        y=i.split('x')
        x = [eval(z) for z in y]
        x.sort()
        print(x)
        l=x[0]
        w=x[1]
        h=x[2]

        lA=l*w
        wA=w*h
        hA=l*h

        total+=((2*l)+(2*w)+(l*w*h))
    print(total)