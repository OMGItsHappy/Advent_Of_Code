f = open("day1.txt", "r")

data = f.readlines()

nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', "1", "2", "3", "4", "5", "6", "7", "8", "9"]

numMap = {"one" : "1" , "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6" : "6", "7" : "7", "8" : "8", "9" : "9"}

import re

def first(line: str):
    minIndex = -1
    best = -1

    for num in nums:
        if num in line:
            if line.index(num) < minIndex or minIndex == -1:
                minIndex = line.index(num)
                best = num
                
    assert best != -1, line        
    return numMap[best]
        
def last(line : str):
    maxIndex = -1
    best = -1
    
    for num in nums:
        if num in line:
            if line[::-1].index(num[::-1]) < maxIndex or maxIndex == -1:
                maxIndex = line[::-1].index(num[::-1])
                best = num
    assert best != -1, line
    return numMap[best]
        
total = 0
        
for line in data:
    # result = re.findall("|".join(nums), line)
    
    #total += int(numMap[result[0]] + numMap[result[-1]]) Should work, it isnt for some reason?
    
    total += int(first(line) + last(line))
    
print(total)