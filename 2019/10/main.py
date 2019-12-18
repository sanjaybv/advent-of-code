from fileinput import input as f_input
from itertools import permutations
from math import atan2

asteroids = [(x, y) for y, line in enumerate(f_input()) 
                for x, c in enumerate(line) if c == '#']

member = set(asteroids)

def scan_asteroids():
    counts = {x: len(asteroids)-1 for x in asteroids}
    vicinity = {}
    for (a, b) in permutations(asteroids, 2):
        if a[1] == b[1]:
            for x in range(min(a[0], b[0]) + 1, max(a[0], b[0])):
                if (x, a[1]) in member:
                    counts[a] -= 1
                    break
            else:
                vicinity[a] = vicinity.get(a, [])
                vicinity[a].append(b)
        elif a[0] == b[0]:
            for y in range(min(a[1], b[1]) + 1, max(a[1], b[1])):
                if (a[0], y) in member:
                    counts[a] -= 1
                    break
            else:
                vicinity[a] = vicinity.get(a, [])
                vicinity[a].append(b)
        else:
            m = (b[1] - a[1]) / (b[0] - a[0])
            c = a[1] - (m * a[0])
            for x in range(min(a[0], b[0]) + 1, max(a[0], b[0])):
                # Stupid floating values requires rounding off. I spent 3+ hours debugging.
                y = round((m * x) + c, 5)
                if (x, y) in member:
                    counts[a] -= 1
                    break
            else:
                vicinity[a] = vicinity.get(a, [])
                vicinity[a].append(b)
    return (counts, vicinity)

counts, vicinity = scan_asteroids()
max_asteroid = max(counts, key=counts.get)
print(max_asteroid, counts[max_asteroid])

# Debugger

def angle(a, b):
    return atan2(b[1] - a[1], b[0] - a[0])

def debug():
    seen = {}
    for ast in vicinity[max_asteroid]:
        a = angle(ast, max_asteroid)
        if a in seen:
            print("???", ast, seen[a])
        else:
            seen[a] = ast
debug()
