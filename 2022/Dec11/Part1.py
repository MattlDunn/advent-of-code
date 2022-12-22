import operator
from typing import List
import re
import math

op_code = {
    '+': operator.add,
    '*': operator.mul,
}


class Monkey:
    def __init__(self, items, operation, test, if_true, if_false):
        self.items: List[str] = items
        self.operation: str = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0

    def do_operation(self, index):
        split = self.operation.split(' ')
        left = split[0]
        op = split[1]
        right = split[2]

        if left == 'old':
            left = self.items[index]
        if right == 'old':
            right = self.items[index]

        self.items[index] = op_code[op](int(left), int(right))
        self.inspected += 1

    def lose_interest(self, index):
        self.items[index] = math.floor(int(self.items[index]) / 3)

    def do_test(self, index):
        if self.items[index] % self.test == 0:
            return True
        else:
            return False


def main():
    in_txt = open('Full.in', 'r')
    monkeys: List[Monkey] = []

    while in_txt.readline().rstrip().lstrip():
        # items
        line = in_txt.readline().rstrip().lstrip()
        items = re.findall(r'\d+', line)
        # operation
        line = in_txt.readline().rstrip().lstrip()
        operation = line.split(' = ')[1]
        # test
        line = in_txt.readline().rstrip().lstrip()
        test = int(re.search(r'\d+', line)[0])
        # if_true
        line = in_txt.readline().rstrip().lstrip()
        if_true = int(re.search(r'\d+', line)[0])
        # if_false
        line = in_txt.readline().rstrip().lstrip()
        if_false = int(re.search(r'\d+', line)[0])

        in_txt.readline()

        monkeys.append(Monkey(items, operation, test, if_true, if_false))

    for _ in range(20):
        for monkey in monkeys:
            for index in range(len(monkey.items)):
                monkey.do_operation(index)
                monkey.lose_interest(index)
                if monkey.do_test(index):
                    monkeys[monkey.if_true].items.append(monkey.items[index])
                else:
                    monkeys[monkey.if_false].items.append(monkey.items[index])

            monkey.items.clear()

    most_inspected = 0
    second_most_inspected = 0
    for monkey in monkeys:
        if monkey.inspected > most_inspected:
            second_most_inspected = most_inspected
            most_inspected = monkey.inspected
        elif monkey.inspected > second_most_inspected:
            second_most_inspected = monkey.inspected

    return most_inspected * second_most_inspected


print(main())
