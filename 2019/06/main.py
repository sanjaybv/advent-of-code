from fileinput import input
from functools import lru_cache

edges = map(lambda x: tuple(x.strip().split(')')), input())

# map from a node to its parent
nodes = {b: a for (a, b) in edges}

@lru_cache(maxsize=None)
def orbits(node):
    parent = nodes.get(node, "")
    return 0 if parent == "" else orbits(parent) + 1


print(sum(orbits(node) for node in nodes.keys()))


