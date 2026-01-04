def is_number_silly(n):
    str_n = str(n)
    len_n = len(str_n)

    if len_n < 2:
        return False

    for pattern_len in range(1, len_n // 2 + 1):
        if len_n % pattern_len == 0:
            pattern = str_n[:pattern_len]
            if pattern * (len_n // pattern_len) == str_n:
                return True

    return False


def sum_ids_for_range(start, end):
    range_id_sum = 0

    for id in range(start, end + 1):
        if is_number_silly(id):
            range_id_sum += id

    return range_id_sum


def main():
    id_sum = 0

    with open("Part2.in") as f:
        line = f.readline()

    ranges = line.split(",")
    for range in ranges:
        split_range = range.split("-")
        id_sum += sum_ids_for_range(int(split_range[0]), int(split_range[1]))

    print(id_sum)


if __name__ == "__main__":
    main()
