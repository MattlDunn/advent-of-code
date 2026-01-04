from typing import List


class Space:
    def __init__(self, elevation, co_ords, is_end=False):
        self.elevation = elevation
        self.co_ords = co_ords
        self.is_end = is_end
        self.moves = float('inf')


board: List[List[Space]] = []


def compute(current: Space):
    global board

    if current.is_end:
        return

    y = current.co_ords[0]
    x = current.co_ords[1]
    potential_children = []
    if y - 1 >= 0:
        potential_children.append(board[y - 1][x])
    if x + 1 < len(board[y]):
        potential_children.append(board[y][x + 1])
    if y + 1 < len(board):
        potential_children.append(board[y + 1][x])
    if x - 1 >= 0:
        potential_children.append(board[y][x - 1])

    for potential_child in potential_children:
        if potential_child.elevation - current.elevation <= 1 and potential_child.moves > current.moves + 1:
            potential_child.moves = current.moves + 1
            compute(potential_child)


def main():
    global board
    in_txt = open('Full.in', 'r')
    start = None
    end = None

    while line := in_txt.readline().rstrip():
        row = []
        for height in line:
            co_ords = (len(board), len(row))
            if height == 'S':
                start = Space(ord('a'), co_ords)
                row.append(start)
            elif height == 'E':
                end = Space(ord('z'), co_ords, True)
                row.append(end)
            else:
                row.append(Space(ord(height), co_ords))
        board.append(row)

    start.moves = 0
    compute(start)

    print(end.moves)


main()
