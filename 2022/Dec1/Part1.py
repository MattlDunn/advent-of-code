in_txt = open('Full.in', 'r')

max_cals = 0
cur = 0

while line := in_txt.readline():
    if line == "\n":
        if cur > max_cals:
            max_cals = cur
        cur = 0

    else:
        cur += int(line)

if cur > max_cals:
    max_cals = cur

print(max_cals)
