with open("input.txt", "r") as f:
    data = f.read().splitlines()

    sums = []
    tmpTotal = 0

    for x in data:
        if x != "":
            tmpTotal+=int(x)
        else:
            sums.append(tmpTotal)
            tmpTotal = 0

    sums.sort()

    print(sum(sums[-3:]))
