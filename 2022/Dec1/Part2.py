in_txt = open('Dec1.in', 'r')

first = 0
second = 0
third = 0
cur = 0

while line := in_txt.readline():
    if line == "\n":
        if cur > first:
            third = second
            second = first
            first = cur
        elif cur > second:
            third = second
            second = cur
        elif cur > third:
            third = cur

        cur = 0

    else:
        cur += int(line)

if cur > first:
    third = second
    second = first
    first = cur
elif cur > second:
    third = second
    second = cur
elif cur > third:
    third = cur


total = first + second + third
print(total)
