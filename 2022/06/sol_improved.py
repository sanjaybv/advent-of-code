import fileinput
from itertools import takewhile

inp = next(iter(fileinput.input()))


def solve(n: int):
    tw = takewhile(lambda i: len(set(inp[i : i + n])) < n, range(0, len(inp) - n))
    return len(list(tw)) + n


# part 1
print(solve(4))
# part 2
print(solve(14))
