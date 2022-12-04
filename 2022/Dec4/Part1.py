in_txt = open('Full.in', 'r')

count = 0

while line := in_txt.readline():
    line = line.rstrip()
    split = line.split(',')
    first_split = split[0].split('-')
    second_split = split[1].split('-')

    first_low = int(first_split[0])
    first_high = int(first_split[1])
    second_low = int(second_split[0])
    second_high = int(second_split[1])

    if first_low == second_low or first_high == second_high:
        count += 1
    elif first_low < second_low:
        if first_high > second_high:
            count += 1
    elif first_low > second_low:
        if first_high < second_high:
            count += 1

print(count)
