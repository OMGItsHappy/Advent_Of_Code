def part1(location : str) -> int:

    f = open(location, "r")

    data = f.read()

    f.close()

    for x in range(len(data)):

        s = set(data[x:x+4])

        if len(s) == 4:
            return x+4

def part2(location) -> int:
    f = open(location, "r")

    data = f.read()

    f.close()

    for x in range(len(data)):

        s = set(data[x:x+14])

        if len(s) == 14:
            return x + 14
