def is_number_silly(n):
    str_n = str(n)
    if len(str_n) % 2 != 0:
        return False

    start_idx = 0
    mid_idx = len(str_n) // 2
    while mid_idx < len(str_n):
        if str_n[start_idx] != str_n[mid_idx]:
            return False

        start_idx += 1
        mid_idx += 1

    return True


def sum_ids_for_range(start, end):
    range_id_sum = 0

    for id in range(start, end + 1):
        if is_number_silly(id):
            range_id_sum += id

    return range_id_sum


def main():
    id_sum = 0

    with open("Part1.in") as f:
        line = f.readline()

    ranges = line.split(",")
    for range in ranges:
        split_range = range.split("-")
        id_sum += sum_ids_for_range(int(split_range[0]), int(split_range[1]))

    print(id_sum)


if __name__ == "__main__":
    main()
