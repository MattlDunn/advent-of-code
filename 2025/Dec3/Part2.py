def get_max_with_idx(arr, start, end):
    max_a = -1
    max_idx = -1

    for idx in range(start, end):
        a = int(arr[idx])
        if a > max_a:
            max_a = a
            max_idx = idx

    return max_a, max_idx


def get_joltage_of_bank(bank, num_to_select):
    digits = ""
    idx = -1

    for i in range(num_to_select):
        digits_remaining = num_to_select - (i + 1)
        next_digit, idx = get_max_with_idx(bank, idx + 1, len(bank) - digits_remaining)
        digits += str(next_digit)

    return int(digits)


def main():
    joltage_sum = 0

    with open("Part2.in") as f:
        while line := f.readline().strip():
            joltage_sum += get_joltage_of_bank(line, 12)

    print(joltage_sum)


if __name__ == "__main__":
    main()
