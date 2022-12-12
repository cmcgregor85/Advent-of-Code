path = "C:\\Users\\Collin\\Desktop\\Advent of Code\\Day10\\Day10_Input.txt"
x=1
cycleCount = 0
internalClock = 1
printer = 20
with open(path) as inputFile:
    input = inputFile.read().splitlines()
    for line in input:
        internalClock=1
        cycleCount+=1
        if cycleCount == printer:
            print(x*printer)
            printer+=40
        if line == "noop":
            continue
        else:
            while internalClock<2:
                if cycleCount == printer:
                    print(x*printer)
                    printer+=40
                cycleCount+=1
                internalClock+=1
                if cycleCount == printer:
                    print(x*printer)
                    printer+=40
            x+=int(line[5:])

    if cycleCount == printer:
        print(x*printer)    

