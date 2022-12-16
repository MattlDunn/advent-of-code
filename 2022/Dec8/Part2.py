in_txt = open('Full.in', 'r')

trees = []


def visible_left(row, col):
    global trees
    value = trees[row][col]
    num_visible = 0
    col -= 1
    while col >= 0:
        num_visible += 1
        if trees[row][col] >= value:
            break
        col -= 1

    return num_visible


def visible_right(row, col):
    global trees
    value = trees[row][col]
    num_visible = 0
    col += 1
    while col < len(trees[row]):
        num_visible += 1
        if trees[row][col] >= value:
            break
        col += 1

    return num_visible


def visible_up(row, col):
    global trees
    value = trees[row][col]
    num_visible = 0
    row -= 1
    while row >= 0:
        num_visible += 1
        if trees[row][col] >= value:
            break
        row -= 1

    return num_visible


def visible_down(row, col):
    global trees
    value = trees[row][col]
    num_visible = 0
    row += 1
    while row < len(trees[col]):
        num_visible += 1
        if trees[row][col] >= value:
            break
        row += 1

    return num_visible


def main():
    while line := in_txt.readline().rstrip():
        row = []
        for height in line:
            row.append(height)

        trees.append(row)

    max_score = 0
    for row_i in range(len(trees)):
        for col_i in range(len(trees[row_i])):
            score = visible_left(row_i, col_i) * visible_right(row_i, col_i) * visible_up(row_i, col_i) * visible_down(row_i, col_i)
            if score > max_score:
                max_score = score

    return max_score


print(main())
