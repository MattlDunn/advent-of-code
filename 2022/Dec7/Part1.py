class Node:
    def __init__(self, value, parent, children) -> None:
        self.value = value
        self.parent = parent
        self.children = children


class Tree:
    def __init__(self) -> None:
        self.root = Node('/', None, [])


total = 0


def get_size(root):
    value = 0
    if root.children == None:
        value = root.value
        return value
    else:
        for child in root.children:
            value += get_size(child)

        if value <= 100000:
            global total
            total += value
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

get_size(tree.root)
print(total)
