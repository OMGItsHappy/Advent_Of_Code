data = open('input.txt', 'r').read().splitlines()

import re

#part 1 _________________________________________________________________

total = 0

cardCopyCount = [ 0 for line in data]

for i, line in enumerate(data):
    winners = set(re.search(r":.*[|]", line).group()[2:-2].split())
    numbers = set(re.search(r"[|].*", line).group()[2:].split())
    cardNum = re.findall(r"\d+[:]", line)[0][:-1]

    matches = winners.intersection(numbers)

    for j, match in enumerate(matches):
        cardCopyCount[i + (j + 1)] += cardCopyCount[i] + 1

    if len(matches) > 0:
        total += 1 * 2 ** (len(matches)-1)

    

print(total)

# part 2 _________________________________________________________________

cardCopyCount = [ copy + 1 for copy in cardCopyCount]
    
print(sum(cardCopyCount))