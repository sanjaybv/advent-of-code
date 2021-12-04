import fileinput
from itertools import combinations

lines = [line.strip() for line in fileinput.input()]
d = {}
x, y = 0, 0
for char in lines[0]:
    d[(x,y)] = d[(x,y)] if (x,y) in d else 1
    if char == '^':
        y += 1
    elif char == 'v':
        y -= 1
    elif char == '>':
        x += 1
    else:
        x -= 1

print(len(d))
