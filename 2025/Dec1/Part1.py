def get_number_from_spin(start, direction, count):
    if direction == "L":
        return (start - count) % 100
    else:
        return (start + count) % 100


def main():
    code = 0

    with open("Part1.in") as f:
        number = 50
        while line := f.readline():
            direction = line[0]
            count = int(line[1:])

            number = get_number_from_spin(number, direction, count)

            if number == 0:
                code += 1

    print(code)


if __name__ == "__main__":
    main()
