import fileinput
from itertools import takewhile

l = next(iter(fileinput.input()))

def solve(n: int):
    for i in range(0, len(l)-n):
        if len(set(l[i:i+n])) >= n:
            return i+n

# part 1
print(solve(4))
# part 2
print(solve(14))
