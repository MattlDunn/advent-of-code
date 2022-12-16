in_txt = open('Full.in', 'r')

trees = []


def check_left(row, col):
    global trees
    value = trees[row][col]
    visible = True
    col -= 1
    while col >= 0:
        if trees[row][col] >= value:
            visible = False
            break
        col -= 1

    return visible


def check_right(row, col):
    global trees
    value = trees[row][col]
    visible = True
    col += 1
    while col < len(trees[row]):
        if trees[row][col] >= value:
            visible = False
            break
        col += 1

    return visible


def check_up(row, col):
    global trees
    value = trees[row][col]
    visible = True
    row -= 1
    while row >= 0:
        if trees[row][col] >= value:
            visible = False
            break
        row -= 1

    return visible


def check_down(row, col):
    global trees
    value = trees[row][col]
    visible = True
    row += 1
    while row < len(trees[col]):
        if trees[row][col] >= value:
            visible = False
            break
        row += 1

    return visible


def main():
    while line := in_txt.readline().rstrip():
        row = []
        for height in line:
            row.append(height)

        trees.append(row)

    num_visible = 0
    for row_i in range(len(trees)):
        for col_i in range(len(trees[row_i])):
            is_visible = check_left(row_i, col_i)
            if not is_visible:
                is_visible = check_right(row_i, col_i)
            if not is_visible:
                is_visible = check_up(row_i, col_i)
            if not is_visible:
                is_visible = check_down(row_i, col_i)

            num_visible += is_visible

    return num_visible


print(main())
