class Node:
    def __init__(self, value, parent, children) -> None:
        self.value = value
        self.parent = parent
        self.children = children


class Tree:
    def __init__(self) -> None:
        self.root = Node('/', None, [])


def get_size(root):
    if root.children == None:
        return root.value
    else:
        value = 0
        for child in root.children:
            value += get_size(child)

        return value


tree = Tree()
current_node = tree.root

in_txt = open('Full.in', 'r')

while line := in_txt.readline().rstrip():
    parts = line.split(' ')
    if parts[0] == '$':
        if parts[1] == 'cd':
            if parts[2] == '/':
                current_node = tree.root
            elif parts[2] == '..':
                current_node = current_node.parent
            else:
                for child in current_node.children:
                    if child.value == parts[2]:
                        current_node = child
    elif parts[0] == 'dir':
        current_node.children.append(Node(parts[1], current_node, []))
    else:
        current_node.children.append(Node(int(parts[0]), current_node, None))

total_size = get_size(tree.root)
smallest = total_size
to_delete = 30000000 - (70000000 - total_size)


def get_smallest_delete(root):
    global smallest
    if root.children == None:
        return root.value
    else:
        value = 0
        for child in root.children:
            value += get_smallest_delete(child)

        if value < smallest and value >= to_delete:
            smallest = value

        return value


get_smallest_delete(tree.root)
print(smallest)
