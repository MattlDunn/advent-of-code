in_txt = open('Full.in', 'r')

sum = 0
should_continue = True

while should_continue:
    group_sack = {}
    for _ in range(3):
        elf_sack = {}
        line = in_txt.readline().rstrip()

        if not line:
            should_continue = False

        for c in line:
            if not c in elf_sack:
                if c in group_sack:
                    group_sack[c] += 1
                    if group_sack[c] == 3:
                        if c.isupper():
                            sum += ord(c) - 38
                        else:
                            sum += ord(c) - 96
                else:
                    group_sack[c] = 1
                elf_sack[c] = True

print(sum)
