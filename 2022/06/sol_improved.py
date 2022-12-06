import fileinput
from itertools import takewhile

l = next(iter(fileinput.input()))

def solve(n: int):
    tw = takewhile(lambda i: len(set(l[i:i+n])) < n, range(0, len(l)-n))
    return len(list(tw)) + n

# part 1
print(solve(4))
# part 2
print(solve(14))
