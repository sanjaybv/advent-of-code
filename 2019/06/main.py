from fileinput import input
from functools import lru_cache

class Node:
    def __init__(self, parent=None):
        self.parent = parent

edges = map(lambda x: tuple(x.strip().split(')')), input())

nodes = {}
for a, b in edges:
    nodes[a] = nodes.get(a, Node())
    nodes[b] = nodes.get(b, Node())
    nodes[b].parent = nodes[a]

@lru_cache(maxsize=None)
def orbits(node):
    return 0 if node.parent == None else orbits(node.parent) + 1

print(sum(orbits(node) for node in nodes.values()))


