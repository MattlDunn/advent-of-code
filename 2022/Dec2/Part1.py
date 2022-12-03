in_txt = open('Full.in', 'r')

you_beat = {
    "X": "C",
    "Y": "A",
    "Z": "B",
}

opponent_beat = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

score = 0
while line := in_txt.readline():
    opponent = line[0]
    you = line[2]
    score += scores[you]

    if you_beat[you] == opponent:
        score += 6
    elif opponent_beat[opponent] == you:
        score += 0
    else:
        score += 3

print(score)