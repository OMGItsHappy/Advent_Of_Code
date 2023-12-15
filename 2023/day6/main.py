data = open("input.txt", "r").read().splitlines()

times = [int(x) for x in data[0].split()[1:]]
dists = [int(x) for x in data[1].split()[1:]]

total = 1

for i, time in enumerate(times):
    time = time
    dist = dists[i]
    
    timeTotal = 0
    
    def calcDist(allowedTime, time):
        tavelPerSec = time
        
        allowedTime = allowedTime - time
        
        return tavelPerSec * allowedTime
    
    for x in range(time):
        if calcDist(time, x) > dist:
            timeTotal += 1
            
    total *= timeTotal
    
print(total)

#part 2


data = open("input.txt", "r").read().splitlines()

times = int(''.join(data[0].split()[1:]))
dists = int(''.join(data[1].split()[1:]))

timeTotal = 0

def calcDist(allowedTime, time):
    tavelPerSec = time
    
    allowedTime = allowedTime - time
    
    return tavelPerSec * allowedTime

for x in range(times):
    if calcDist(times, x) > dists:
        timeTotal += 1
            
print(timeTotal)