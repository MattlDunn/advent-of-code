in_txt = open('Full.in', 'r')

you_beat = {
    "A": 2,
    "B": 3,
    "C": 1,
}

you_lose = {
    "A": 3,
    "B": 1,
    "C": 2,
}

you_draw = {
    "A": 1,
    "B": 2,
    "C": 3,
}

score = 0
while line := in_txt.readline():
    opponent = line[0]
    result = line[2]

    if (result == "X"):
        score += you_lose[opponent]
    elif(result == "Y"):
        score += you_draw[opponent]
        score += 3
    else:
        score += you_beat[opponent]
        score += 6

print(score)