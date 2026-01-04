def get_number_from_spin(start, direction, count):
    if direction == "L":
        end_number = (start - count) % 100
        times_passed = ((100 - start) % 100 + count) // 100
    else:
        end_number = (start + count) % 100
        times_passed = (start + count) // 100

    return end_number, times_passed


def main():
    code = 0

    with open("Part2.in") as f:
        number = 50
        while line := f.readline():
            direction = line[0]
            count = int(line[1:])

            number, times_passed = get_number_from_spin(number, direction, count)

            code += times_passed

    print(code)


if __name__ == "__main__":
    main()
