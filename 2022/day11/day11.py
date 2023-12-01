import functools

class monkey:
    def __init__(self, data : list[str]) -> None:
        tmp = data.pop(0)

        self.number = int(tmp[tmp.find(" ") + 1 : tmp.find(":")])

        tmp = data.pop(0)

        self.items = list(map(int, tmp[tmp.find(":") + 1:].split(", ")))

        tmp = data.pop(0).split()

        try: self.num = int(tmp[-1])
        except : pass

        if tmp[-1] == "old":
            self.operation = lambda x: x*x

        elif tmp[-2] == "+":
            self.operation = lambda x: x + self.num
        elif tmp[-2] == "*":
            self.operation = lambda x : x * self.num

        self.div = int(data.pop(0).split()[-1])
        self.m1 = int(data.pop(0).split()[-1])
        self.m2 = int(data.pop(0).split()[-1])

        self.test = lambda x: self.m1 if x % self.div == 0 else self.m2

        self.examined = 0



def part1(location : str) -> int:
    f = open(location, "r")

    data = f.read().splitlines()

    f.close()

    monekys = []

    tmp = []

    for line in data:
        if line != "":
            tmp.append(line)
        else :
            monekys.append(monkey(tmp))
            tmp = []

    monekys.append(monkey(tmp))

    round = 0
    i = 0

    while round < 20:
        for monk in monekys:
            for item in monk.items:
                item = monk.operation(item)
                
                #item = int(item/3)
                monekys[monk.test(item)].items.append(item)
                monekys[i].examined += 1

            monekys[monk.number].items = []
            i += 1

        round += 1
        if round%100 == 0: print(round)
        i = 0

    p = sorted([x.examined for x in monekys])

    print(p)

    return p[-1] * p[-2]

class monkey2:
    def __init__(self, data : list[str]) -> None:
        tmp = data.pop(0)

        self.number = int(tmp[tmp.find(" ") + 1 : tmp.find(":")])

        tmp = data.pop(0)

        self.items = list(map(int, tmp[tmp.find(":") + 1:].split(", ")))

        tmp = data.pop(0).split()

        try: self.num = int(tmp[-1])
        except : pass

        if tmp[-1] == "old":
            self.operation = lambda x: x*x

        elif tmp[-2] == "+":
            self.operation = lambda x: x + self.num
        elif tmp[-2] == "*":
            self.operation = lambda x : x * self.num

        self.div = int(data.pop(0).split()[-1])
        self.m1 = int(data.pop(0).split()[-1])
        self.m2 = int(data.pop(0).split()[-1])

        self.test = lambda x: self.m1 if x % self.div == 0 else self.m2

        self.examined = 0

def part2(location : str) -> int:
    f = open(location, "r")

    data = f.read().splitlines()

    f.close()

    monekys = []

    tmp = []

    for line in data:
        if line != "":
            tmp.append(line)
        else :
            monekys.append(monkey2(tmp))
            tmp = []

    monekys.append(monkey2(tmp))

    round = 0
    i = 0

    while round < 20:
        for monk in monekys:
            for item in monk.items:
                item = monk.operation(item)
                
                #item = int(item/3)
                monekys[monk.test(item)].items.append(item)
                monekys[i].examined += 1

            monekys[monk.number].items = []
            i += 1

        round += 1
        if round%100 == 0: print(round)
        i = 0

    p = sorted([x.examined for x in monekys])

    print(p)

    return p[-1] * p[-2]

print(part1("input.txt"))