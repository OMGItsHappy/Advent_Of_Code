def part1(location : str) -> int:

    f = open(location, "r")

    data = f.read().splitlines()

    f.close()

    for i in range(len(data)):
        data[i] = [int(num) for num in data[i]]

    total = 0

    for row in range(len(data)):
        for col in range(len(data[row])):

            checked = 0

            currNum = data[row][col]

            # left

            for tree in range(0, col):
                if data[row][tree] >= currNum:
                    checked += 1
                    break
            #right

            for tree in range(col+1, len(data[0])):
                if data[row][tree] >= currNum:
                    checked += 1
                    break

            #up

            for tree in range(0, row):
                if data[tree][col] >= currNum:
                    checked += 1
                    break

            

            for tree in range(row + 1, len(data)):
                if data[tree][col] >= currNum:
                    checked += 1
                    break

            if checked == 4:
                total += 1

    return (row+1) * (col+1) - total

def part2(location : str) -> int:

    f = open(location, "r")

    data = f.read().splitlines()

    f.close()

    for i in range(len(data)):
        data[i] = [int(num) for num in data[i]]

    m = 0

    for row in range(len(data)):
        for col in range(len(data[row])):

            dists = []

            currNum = data[row][col]

            # left
            tmp = 0
            for tree in range(col - 1, -1, -1):
                tmp += 1
                if data[row][tree] >= currNum:
                    break
            dists.append(tmp)
            tmp = 0
            #right

            for tree in range(col+1, len(data[0])):
                tmp += 1
                if data[row][tree] >= currNum:
                    break

            dists.append(tmp)
            tmp = 0
            #up

            for tree in range(row-1, -1, -1):
                tmp += 1
                if data[tree][col] >= currNum:
                    break
            
            dists.append(tmp)
            tmp = 0

            for tree in range(row + 1, len(data)):
                tmp += 1
                if data[tree][col] >= currNum:
                    break
            dists.append(tmp)

            tmp = 1

            for x in dists:
                tmp*=x

            if tmp > m:
                m = tmp

    return m


def test(data, row, col):

    dists = []

    currNum = data[row][col]

    # left
    tmp = 0
    for tree in range(col - 1, -1, -1):
        tmp += 1
        if data[row][tree] >= currNum:
            break

    dists.append(tmp)
    tmp = 0
    #right

    for tree in range(col+1, len(data[0])):
        tmp += 1
        if data[row][tree] >= currNum:
            break

    dists.append(tmp)
    tmp = 0
    #up
    for tree in range(row - 1, -1, -1):
        tmp += 1
        if data[tree][col] >= currNum:
            break
    
    dists.append(tmp)
    tmp = 0

    for tree in range(row + 1, len(data)):
        tmp += 1
        if data[tree][col] >= currNum:
            break

    dists.append(tmp)

    m = 1

    for x in dists:
        m*=x

    return m

print(part2("input.txt"))
