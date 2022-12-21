in_txt = open('Full.in', 'r')

cycle = 0
score_sum = 0
register = 1

while line := in_txt.readline().rstrip():
    if line == 'noop':
        cycle += 1
        if (cycle - 20) % 40 == 0:
            score_sum += cycle * register
    else:
        for _ in range(2):
            cycle += 1
            if (cycle - 20) % 40 == 0:
                score_sum += cycle * register

        register += int(line.split(' ')[1])

print(score_sum)
