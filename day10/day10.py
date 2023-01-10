def part1(location : str) -> int:
    f = open(location, "r")

    data = map(lambda x : x.split(" "), f.read().splitlines())
    data = list(map(lambda x : [x[0]] if len(x) == 1 else [x[0], int(x[1])], data))

    f.close()

    cycles = 0

    x = 1

    sumOfX = 0

    toCheck = 20

    for instruction in data:

        if instruction[0] == "noop":
            cycles += 1
        else:

            for y in range(2):
                cycles += 1
                if cycles >= toCheck:
                    print(x)
                    sumOfX += (x * toCheck)
                    toCheck += 40
                    
                

            x += instruction[1]




    
    return(sumOfX)


def part2(location : str) -> int:
    f = open(location, "r")

    data = map(lambda x : x.split(" "), f.read().splitlines())
    data = list(map(lambda x : [x[0]] if len(x) == 1 else [x[0], int(x[1])], data))

    f.close()

    currCycles = -1

    x = 1

    currPixel = -1

    crtRows = ["" for row in range(6)]

    for line in data:

        for cycle in range(2):

            currPixel += 1

            if abs(currPixel%40 - x) < 2:
                crtRows[int(currPixel/40)] += "#"
            else:
                crtRows[int(currPixel/40)] += "."

            if line[0] == "noop":
                break
            elif cycle == 1:    
                x += line[1]
            

    return crtRows




        




for x in part2("input.txt"):
    print(x)
