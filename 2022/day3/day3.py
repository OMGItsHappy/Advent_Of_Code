def toInt(ch : str) -> int:
    if ch.islower():
        return ord(ch) - ord("a") + 1
    elif ch.isupper:
        return ord(ch) - ord("A") + 27

def part1(fileLocation : str) -> int:

    return sum([toInt(set(x[:int(len(x)/2)]).intersection(set(x[int(len(x)/2):])).pop()) for x in open(fileLocation, "r").read().splitlines()])
    
def part2(fileLocation:str) -> int:
    f = open(fileLocation, "r")

    f = f.read().splitlines()

    tmp = [set(f.pop(0))]

    while len(f) != 0:
        tmp[-1] = tmp[-1].intersection(set(f.pop(0)))

        if len(f)%3 == 0 and len(f) != 0: tmp.append(set(f.pop(0)))

    return sum([toInt(x.pop()) for x in tmp])


print(part1("input.txt"))
