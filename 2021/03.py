from typing import Counter
import numpy
import fileinput

numbers = [list(line.strip()) for line in fileinput.input()]

def gamma_epsilon(numbers):
    g, e = [], []
    for col in numpy.transpose(numbers):
        c = Counter(col).most_common()
        g.append(c[0][0])
        e.append(c[-1][0])
    return int(''.join(g), base=2), int(''.join(e), base=2)


# node is a trie node
class node(object):
    def __init__(self) -> None:
        self.count:int = 0
        self.children:dict = {}
        super().__init__()

    def add(self, path, value):
        if len(path) == 0:
            self.value = value
            return
        self.count += 1
        if path[0] not in self.children:
            self.children[path[0]] = node()
        self.children[path[0]].add(path[1:], value)

def most(root: node):
    if len(root.children) == 0:
        return root.value
    largest = None
    for bit, child in root.children.items():
        if not largest \
            or child.count > largest[1].count \
            or (child.count == largest[1].count and bit > largest[0]):
            largest = (bit, child)
    return most(largest[1])

def least(root: node):
    if len(root.children) == 0:
        return root.value
    smallest = None
    for bit, child in root.children.items():
        if not smallest \
            or child.count < smallest[1].count \
            or (child.count == smallest[1].count and bit < smallest[0]):
            smallest = (bit, child)
    return least(smallest[1])

# part 1
print(numpy.prod(gamma_epsilon(numbers)))

# part 2
root = node()
for n in numbers:
    root.add(n, ''.join(n))
m, l = int(most(root), 2), int(least(root), 2)
print(m * l)
