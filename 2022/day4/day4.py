def part1(location : str) -> int:
    f = open(location, "r")

    data = f.read().splitlines()

    f.close()

    total = 0
    
    for r in data:
        r = r.split(',')

        tmp = []

        for nums in r:
            nums = nums.split("-")
            tmp.append(int(nums[0]))
            tmp.append(int(nums[1]))

        if (tmp[0] <= tmp[2] and tmp[1] >= tmp[3]) or (tmp[0] >= tmp[2] and tmp[1] <= tmp[3]):
            total += 1
            print(tmp)

    return total

def part2(location : str) -> int:
    f = open(location, "r")

    data = f.read().splitlines()

    f.close()

    total = 0
    
    for r in data:
        r = r.split(',')

        tmp = []

        for nums in r:
            nums = nums.split("-")
            tmp.append(int(nums[0]))
            tmp.append(int(nums[1]))

        if len(set(range(tmp[0], tmp[1] + 1)).intersection(set(range(tmp[2], tmp[3] + 1)))) > 0:
            total += 1
            
    print(total)



part2("input.txt")