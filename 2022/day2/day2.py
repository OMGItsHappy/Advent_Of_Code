def part1(fileLoaction : str) -> int:
    
    scores = {"X" : 1, "Y" : 2, "Z" : 3, "W" : 6, "L" : 0, "T" : 3}
    eq = {"X" : "A", "Y" : "B", "Z" : "C"}

    wL = ["A Y", "B Z", "C X"]
    tie = ["A X", "B Y", "C Z"]

    f = open(fileLoaction, "r")

    f = f.read().splitlines()

    score = 0

    for x in f:

        score += scores[x[-1]]

        if x in wL: score += 6
        elif x in tie: score += 3
        else: score += 0

    return score

def part2(fileLocation : str) -> int:

    f = open(fileLocation, "r").read().splitlines()

    score = 0

    wL = {"X" : 0, "Y" : 3, "Z" : 6}
    scores = {"X" : 1, "Y" : 2, "Z" : 3}
    draw = {"A" : "X", "B" : "Y", "C" : "Z"}
    win = {"A" : "Y", "B" : "Z", "C" : "X"}
    lose = {"A" : "Z", "B" : "X", "C" : "Y"}
    choose = {"X" : lose, "Y" : draw, "Z" : win}

    for x in f:
        score += wL[x[-1]]

        score += scores[choose[x[-1]][x[0]]]

        #print(score, choose[x[-1]][x[0]])

    return score


print(part2("input.txt"))

        