from typing import List


class Space:
    def __init__(self, elevation, co_ords):
        self.elevation = elevation
        self.co_ords = co_ords

    def __eq__(self, other):
        return self.co_ords == other.co_ords

    def __hash__(self):
        return hash(self.co_ords)


def main():
    in_txt = open('Full.in', 'r')
    board: List[List[Space]] = []
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
                end = Space(ord('z'), co_ords)
                row.append(end)
            else:
                row.append(Space(ord(height), co_ords))
        board.append(row)

    spt = {
        start: 0
    }
    just_added: List[Space] = [start]
    while end not in spt:
        adj = []
        valid_adj = []

        for node in just_added:
            y = node.co_ords[0]
            x = node.co_ords[1]
            if y - 1 >= 0:
                adj.append(board[y - 1][x])
            if x + 1 < len(board[y]):
                adj.append(board[y][x + 1])
            if y + 1 < len(board):
                adj.append(board[y + 1][x])
            if x - 1 >= 0:
                adj.append(board[y][x - 1])

            for adj_node in adj:
                moves = spt[node] + 1
                if adj_node.elevation - node.elevation <= 1 and adj_node not in spt:
                    spt[adj_node] = moves
                    valid_adj.append(adj_node)

        just_added = valid_adj

    print(spt[end])


main()
