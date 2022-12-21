class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"


def main():
    in_txt = open('Full.in', 'r')
    head = Point(0, 0)
    tail = Point(0, 0)
    visited = {Point(tail.x, tail.y): True}

    while line := in_txt.readline().rstrip():
        parts = line.split(' ')
        direction = parts[0]
        moves = int(parts[1])

        for _ in range(moves):
            if direction == 'R':
                head.x += 1
            elif direction == 'L':
                head.x -= 1
            elif direction == 'U':
                head.y += 1
            elif direction == 'D':
                head.y -= 1
            else:
                print('Invalid direction.')

            x_diff = head.x - tail.x
            y_diff = head.y - tail.y
            is_touching = abs(x_diff) < 2 and abs(y_diff) < 2

            if not is_touching:
                if x_diff != 0:
                    tail.x += x_diff / abs(x_diff)
                if y_diff != 0:
                    tail.y += y_diff / abs(y_diff)

            visited[Point(tail.x, tail.y)] = True

    return len(visited)


print(main())

