def get_joltage_of_bank(bank):
    first_digit = max(bank[:-2])
    first_digit_idx = bank.find(first_digit)
    second_digit = max(bank[first_digit_idx + 1:])

    return int(first_digit + second_digit)


def main():
    joltage_sum = 0

    with open("Part1.in") as f:
        while line := f.readline():
            joltage_sum += get_joltage_of_bank(line)

    print(joltage_sum)

if __name__ == "__main__":
    main()
