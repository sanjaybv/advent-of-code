from fileinput import input
from functools import lru_cache

edges = map(lambda x: tuple(x.strip().split(')')), input())
nodes = {b: a for (a, b) in edges} # map from a node to its parent

@lru_cache(maxsize=None)
def orbits(node):
    parent = nodes.get(node, "")
    return 0 if parent == "" else orbits(parent) + 1

print(sum(orbits(node) for node in nodes.keys()))

def ancestors(node):
    anc = []
    while node in nodes:
        anc.append(nodes[node])
        node = nodes[node]
    return anc

def common_ancestor():
    for i, y in enumerate(ancestors("YOU")):
        for j, s in enumerate(ancestors("SAN")):
            if y == s:
                return i + j

print(common_ancestor())
