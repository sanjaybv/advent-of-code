import fileinput
from typing import Tuple
import math


def read_pos(pos: str) -> Tuple[int, int]:
    parts = pos.strip().split(',')
    return (int(parts[0]), int(parts[1]))


def read_line(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    parts = line.strip().split('->')
    return (read_pos(parts[0]), read_pos(parts[1]))

def add_point(points: dict, pos: Tuple[int, int]):
    if pos not in points:
        points[pos] = 1
    else:
        points[pos] += 1

def dist(a, b):
    return math.sqrt(math.pow(a[0]-b[0], 2) + math.pow(a[1]-b[1], 2))

def nav(a, b):
    sx, sy = b[0]-a[0], b[1]-a[1]
    if sx != 0:
        sx /= abs(sx)
    if sy != 0:
        sy /= abs(sy)
    sx, sy = int(sx), int(sy)

    x, y = a[0], a[1]
    while dist(a, (x, y)) + dist((x, y), b) <= dist(a, b) + 0.1:
        yield (x, y)
        x += sx
        y += sy

def main():
    points = {}
    for line in fileinput.input():
        a, b = read_line(line)
        if a[0] == b[0] or a[1] == b[1] or abs(b[1] - a[1]) == abs(b[0] - a[0]):
            for p in nav(a, b):
                add_point(points, p)

    print(len([x for x in filter(lambda x: x > 1, points.values())]))

if __name__ == '__main__':
    main()
