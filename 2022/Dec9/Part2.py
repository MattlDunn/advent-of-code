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
    nodes = [Point(0, 0) for i in range(10)]
    visited = {Point(nodes[0].x, nodes[0].y): True}

    while line := in_txt.readline().rstrip():
        parts = line.split(' ')
        direction = parts[0]
        moves = int(parts[1])

        for _ in range(moves):
            if direction == 'R':
                nodes[0].x += 1
            elif direction == 'L':
                nodes[0].x -= 1
            elif direction == 'U':
                nodes[0].y += 1
            elif direction == 'D':
                nodes[0].y -= 1
            else:
                print('Invalid direction.')

            for i in range(len(nodes) - 1):
                x_diff = nodes[i].x - nodes[i + 1].x
                y_diff = nodes[i].y - nodes[i + 1].y
                is_touching = abs(x_diff) < 2 and abs(y_diff) < 2

                if not is_touching:
                    if x_diff != 0:
                        nodes[i + 1].x += x_diff / abs(x_diff)
                    if y_diff != 0:
                        nodes[i + 1].y += y_diff / abs(y_diff)

            visited[Point(nodes[9].x, nodes[9].y)] = True

    return len(visited)


print(main())

