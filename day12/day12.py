
def part1(location : str) -> int:

    f = open(location, "r")

    data = f.read().splitlines()

    f.close()

    start = [0,0]
    end = [0,0]

    data = list(map(lambda x : list(x), data))

    for row in range(len(data)):
        for col in range(len(data[row])):

            if data[row][col] == "S":
                start = [row, col]
                data[row][col] = 0

            elif data[row][col] == "E":
                end = [row, col]
                data[row][col] = ord("z") - ord("a")

            else: data[row][col] = ord(data[row][col]) - ord("a")
            
    return rec([[start]], data, end, [])

    #print(data)

def rec(possibleMoves : list[list[list[int, int]]], data : list[list[int]], end, valid) :
    newMoves = []
    #print(possibleMoves)
    #print(possibleMoves)

    for moves in possibleMoves:
        spot = moves[-1]
        for row in range(-1, 2):
            for col in range(-1, 2):
                if abs(row) + abs(col) != 2:
                    try:
                        if abs(data[spot[0]][spot[1]] - data[spot[0] + row][spot[1] + col]) < 2 and [spot[0] + row, spot[1] + col] not in moves:
                            tmpMoves = moves
                            tmpMoves.append(([spot[0] + row, spot[1] + col]))
                            newMoves.append(tmpMoves)
                    except IndexError:
                        pass

    for moves in newMoves:
        if moves[-1] == end:
            valid.append(moves)
            newMoves.remove(moves)

    if len(newMoves) == 0: return valid
    
    return rec(newMoves, data, end, valid)


print(part1("example.txt"))