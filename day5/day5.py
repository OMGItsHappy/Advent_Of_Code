def part1(location:str) -> str:

    f = open(location, "r")

    data = f.read().splitlines()

    f.close()

    i = 0

    while data[i] != "": #finding break between blocks and move commands
        i += 1

    lists = [] # lists with blocks

    for x in range(int(data[i-1].split(" ")[-2])): #adding APPROPRAITE NUmber of lists to contain blocks
        lists.append([]) 

    for z in data[:i-1]: # inserting blocks into stacks
        index = 0 # which stack we are looking at
        y = -1 # start at -1 so its consitant
        while y < len(z):
            y += 4
            if z[y-1] == " ":
                pass
            else:
                lists[index].append(z[y-2]) # adding to back of stack
            index += 1

    for line in data[i+1:]: # all the move commands
        line = line.split(" ") # allows for easy indexing of command

        #print(line)

        count = int(line[1]) # how much to move
        fr = int(line[3]) - 1 #intial stack
        to = int(line[5]) - 1# stack to move crates too

        tmp = lists[fr][:count] # the blocks to move

        for letter in tmp: # move each crate indivitually 
            #print(letter, count , fr, to, tmp)
            lists[to].insert(0, letter) # start of list is top of stack

        #lists[to].insert(0, lists[fr][:count])
        lists[fr] = lists[fr][count:] # remove crates from orgin

    tmp = ""

    for li in lists: # output tops of stacks to crates
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

        for letter in tmp[::-1]: # step through backwards to immitate moving in one block
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
