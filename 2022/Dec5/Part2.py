class Stack:
    def __init__(self, start=[]):
        self.data = start

    def pop(self, times):
        popped = []

        for _ in range(times):
            popped.append(self.data.pop())

        popped.reverse()
        return popped

    def push(self, items):
        for item in items:
            self.data.append(item)

    def top(self):
        return self.data[len(self.data) - 1]


in_txt = open('Full.in', 'r')

# stacks = [
#     Stack(['Z', 'N']),
#     Stack(['M', 'C', 'D']),
#     Stack(['P']),
# ]

stacks = [
    Stack(['T', 'P', 'Z', 'C', 'S', 'L', 'Q', 'N']),
    Stack(['L', 'P', 'T', 'V', 'H', 'C', 'G']),
    Stack(['D', 'C', 'Z', 'F']),
    Stack(['G', 'W', 'T', 'D', 'L', 'M', 'V', 'C']),
    Stack(['P', 'W', 'C']),
    Stack(['P', 'F', 'J', 'D', 'C', 'T', 'S', 'Z']),
    Stack(['V', 'W', 'G', 'B', 'D']),
    Stack(['N', 'J', 'S', 'Q', 'H', 'W']),
    Stack(['R', 'C', 'Q', 'F', 'S', 'L', 'V']),
]

while line := in_txt.readline().rstrip():
    for stack in stacks:
        print(stack.data)

    split_line = line.split(' ')
    num = int(split_line[1])
    orig = int(split_line[3])
    new = int(split_line[5])

    top = stacks[orig - 1].pop(num)
    stacks[new - 1].push(top)

all_tops = ""
for stack in stacks:
    all_tops += stack.top()

print(all_tops)
