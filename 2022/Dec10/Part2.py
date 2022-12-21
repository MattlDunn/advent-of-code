def print_pixel(cycle, register):
    if abs(((cycle - 1) % 40) - register) <= 1:
        print('#', end='')
    else:
        print('.', end='')

    if cycle % 40 == 0:
        print('\n', end='')


def main():
    in_txt = open('Full.in', 'r')

    cycle = 0
    register = 1

    while line := in_txt.readline().rstrip():
        if line == 'noop':
            cycle += 1
            print_pixel(cycle, register)
        else:
            for _ in range(2):
                cycle += 1
                print_pixel(cycle, register)

            register += int(line.split(' ')[1])


main()
