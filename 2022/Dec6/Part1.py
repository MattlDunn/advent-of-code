in_txt = open('Full.in', 'r')
line = in_txt.readline().rstrip()

index = 0
unique_count = 0
char_at_index = {}

while index < len(line):
    if unique_count == 4:
        break

    if line[index] in char_at_index:
        index = char_at_index[line[index]] + 1
        char_at_index = {}
        unique_count = 0
    else:
        char_at_index[line[index]] = index
        unique_count += 1
        index += 1

print(index)
