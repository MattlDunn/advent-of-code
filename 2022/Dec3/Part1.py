in_txt = open('Dec3.in', 'r')

sum = 0

while line := in_txt.readline():
    line = line.rstrip()
    first = line[:int(len(line) / 2)]
    second = line[int(len(line) / 2):]

    in_first = {}
    in_second = {}

    for c in first:
        in_first[c] = True

    for c in second:
        if c in in_first and not c in in_second:
            if c.isupper():
                sum += ord(c) - 38
            else:
                sum += ord(c) - 96
        in_second[c] = True


print(sum)
