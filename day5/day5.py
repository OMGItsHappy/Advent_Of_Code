def part1(location:str) -> str:

    f = open(location, "r")

    data = f.read().splitlines()

    f.close()

    i = 0

    while data[i] != "":
        i += 1

    lists = []

    for x in range(int(data[i-1].split(" ")[-2])):
        lists.append([])
    
    for x in data:
        pass
        #print(x)

    for z in data[:i-1]:
        index = 0
        y = -1
        while y < len(z):
            y += 4
            if z[y-1] == " ":
                pass
                #lists[index].append(None)
            else:
                lists[index].append(z[y-2])
            index += 1

    for line in data[i+1:]:
        line = line.split(" ")

        #print(line)

        count = int(line[1])
        fr = int(line[3]) - 1
        to = int(line[5]) - 1

        tmp = lists[fr][:count]

        for letter in tmp:
            #print(letter, count , fr, to, tmp)
            lists[to].insert(0, letter)

        #lists[to].insert(0, lists[fr][:count])
        lists[fr] = lists[fr][count:]

    tmp = ""

    for li in lists:
        try:
            tmp += li[0]
        except:
            pass

    return tmp

def part2(location:str) -> str:

    f = open(location, "r")

    data = f.read().splitlines()

    f.close()

    i = 0

    while data[i] != "":
        i += 1

    lists = []

    for x in range(int(data[i-1].split(" ")[-2])):
        lists.append([])
    
    for x in data:
        pass
        #print(x)

    for z in data[:i-1]:
        index = 0
        y = -1
        while y < len(z):
            y += 4
            if z[y-1] == " ":
                pass
                #lists[index].append(None)
            else:
                lists[index].append(z[y-2])
            index += 1

    for line in data[i+1:]:
        line = line.split(" ")

        #print(line)

        count = int(line[1])
        fr = int(line[3]) - 1
        to = int(line[5]) - 1

        tmp = lists[fr][:count]

        for letter in tmp[::-1]:
            #print(letter, count , fr, to, tmp)
            lists[to].insert(0, letter)

        #lists[to].insert(0, lists[fr][:count])
        lists[fr] = lists[fr][count:]

    tmp = ""

    for li in lists:
        try:
            tmp += li[0]
        except:
            pass

    return tmp


print(part2("input.txt"))
