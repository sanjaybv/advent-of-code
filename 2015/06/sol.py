import fileinput as fi
import re

lines = [line.strip() for line in fi.input()]
pattern = r"^(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)$"

args = []
for line in lines:
    m = re.match(pattern, line)
    if not m:
        continue
    args.append((m.group(1), tuple(map(int, m.groups()[1:5]))))
print("len(args)", len(args))


def do(lights, coords, op):
    for i in range(coords[0], coords[2] + 1):
        for j in range(coords[1], coords[3] + 1):
            lights[i][j] = op(lights[i][j])
    return lights


def part1():
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for arg in args:
        match arg[0]:
            case "turn on":
                lights = do(lights, arg[1], lambda _: 1)
            case "turn off":
                lights = do(lights, arg[1], lambda _: 0)
            case "toggle":
                lights = do(lights, arg[1], lambda x: 1 - x)

    print(sum([sum(row) for row in lights]))


def part2():
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for arg in args:
        match arg[0]:
            case "turn on":
                lights = do(lights, arg[1], lambda x: x + 1)
            case "turn off":
                lights = do(lights, arg[1], lambda x: max(0, x - 1))
            case "toggle":
                lights = do(lights, arg[1], lambda x: x + 2)

    print(sum([sum(row) for row in lights]))


part1()
part2()
