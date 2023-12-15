import re
f = __file__
print(f)
print()

f = open(r"input.txt", "r")

data = f.readlines()

# part 1

bad = set()
good = set()

for game in data:
    pulls = re.split(r"[:;]", game)
    gameNum = re.search(r"\d+", pulls[0]).group()
    badPull = False
    for pull in pulls[1:]:
        
        pull = pull.strip().split(",")
        total = {"red" : 0, "green" : 0, "blue" : 0}
        for pullNum in pull:
            pullNum = pullNum.strip()
            num, color = pullNum.split(" ")
            total[color] += int(num)
        
        maxes = {"red" : 12, "green" : 13, "blue" : 14}
        for color in total:
            if total[color] > maxes[color]:
                badPull = True
    
    if badPull:
        bad.add(int(gameNum))
    else:
        good.add(int(gameNum))
                
print(sum(good))

# part 2

total = 0

for game in data:
    pulls = re.split(r"[:;]", game)
    gameNum = re.search(r"\d+", pulls[0]).group()
    minPulled = {"red" : 0, "green" : 0, "blue" : 0}
    for pull in pulls[1:]:
        
        pull = pull.strip().split(",")
        for pullNum in pull:
            pullNum = pullNum.strip()
            num, color = pullNum.split(" ")
            minPulled[color] = max(int(num), minPulled[color])
        
    from functools import reduce
        
    total += reduce(lambda x,y: x * y, minPulled.values())
     
print(total)