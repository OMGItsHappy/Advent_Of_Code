data = open('input.txt', 'r').read().split('\n')

import re

numsFound = []
charsFound = []

for i, line in enumerate(data):
    nums = re.finditer(r'\d+', line)

    chars = re.finditer(r'[^\d.]', line)

    numsFound.extend([(i, num.start(), num.group(), len(num.group())) for num in nums])

    charsFound.extend([[i, char.start(), char.group()] for char in chars])

total = 0

# part 1 _________________________________________________________________

for num in numsFound:
    for char in charsFound:
        if abs(char[0] - num[0]) < 2 and (char[1] >= num[1] - 1 and char[1] <= num[1] + num[3]):
            total += int(num[2])
            break

print(total)

total = 0

# Part 2 _________________________________________________________________

for num in numsFound:
    for i, char in enumerate(charsFound):
        if abs(char[0] - num[0]) < 2 and (char[1] >= num[1] - 1 and char[1] <= num[1] + num[3]):
            charsFound[i].append(num[2])

for char in charsFound:
    if len(char) == 5 and char[2] == "*":
        total += int(char[-1]) * int (char[-2])

print(total)
            

