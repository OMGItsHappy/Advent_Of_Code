def part1(location : str) ->int:

    f = open(location, "r")

    data = list(map(lambda x: x.split(), f.read().splitlines()))
    data = map(lambda x: [x[0], int(x[1])], data)

    f.close()

    visited = set()
    visited.add("0 0")

    t = [0, 0]
    h = [0, 0] #row col

    pT = [0,0]

    for line in data:
        for move in range(line[1]):

            if line[0] == "R":
                h[1] += 1
            elif line[0] == "L":
                h[1] -= 1
            elif line[0] == "U":
                h[0] -= 1
            elif line[0] == "D":
                h[0] += 1

            if ((h[0] - t[0])**2 + (h[1] - t[1])**2) ** (1/2) >= 2**(1/2) + .1:
                t = pT

            visited.add(f"{t[0]} {t[1]}")
            pT = list(h)

    return visited

def part2(location : str) -> int:
    f = open(location, "r")

    data = list(map(lambda x: x.split(), f.read().splitlines()))
    data = list(map(lambda x: [x[0], int(x[1])], data))

    f.close()

    locs = set()

    preLocs = [[0, 0] for x in range(0, 10)]
    tLocs = [[0, 0] for x in range(0, 10)]

    for line in data:
        for move in range(line[1]):

            if line[0] == "R":
                tLocs[0][1] += 1
            elif line[0] == "L":
                tLocs[0][1] -= 1
            elif line[0] == "U":
                tLocs[0][0] -= 1
            elif line[0] == "D":
                tLocs[0][0] += 1

            for x in range(len(tLocs)-1):

                t = list(tLocs[x+1])
                h = list(tLocs[x+0])
                tmp = list(t)

                if ((h[0] - (t[0]))**2 + ((h[1] - (t[1]))**2)) ** (1/2) >= 2**(1/2) + .1:

                    dist = ((h[0] - (t[0]))**2 + ((h[1] - (t[1]))**2)) ** (1/2)

                    for row in range(-1, 2):
                        for col in range(-1, 2):

                            if ((h[0] - (t[0]+row))**2 + ((h[1] - (t[1]+col))**2)) ** (1/2) <= dist:
                                tmp[0] = t[0]+row
                                tmp[1] = t[1]+col
                                dist = ((h[0] - (t[0]+row))**2 + ((h[1] - (t[1]+col))**2)) ** (1/2)

                tLocs[x+1][0] = tmp[0]
                tLocs[x+1][1] = tmp[1]

            locs.add(f'{tLocs[-1]}')
    return locs

            
            

    #print(tLocs)


    


print(len(part2("input.txt")))