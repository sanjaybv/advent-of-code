import fileinput
from itertools import tee
from copy import deepcopy as dcopy
import re

lines = [l.rstrip('\n') for l in fileinput.input()]

sl = lines[:lines.index('')]
stacks = []
for col in range(1, len(sl[-1]), 4):
    stacks.append(list(filter(str.isalpha, map(
        lambda row: sl[row][col], range(len(sl) - 2, -1, -1)
    ))))


ins = list(map(int, re.findall(r"\d+", l)) for l in lines[lines.index('')+1:])

def solve(ins, s, func):
    for i in ins:
        a, f, t = list(i)
        s[t-1].extend(func(s[f-1][-a:]))
        s[f-1] = s[f-1][:-a]
    print(''.join([j.pop() for j in s]))

# part 1
solve(dcopy(ins), dcopy(stacks), reversed)

# part 2
solve(dcopy(ins), dcopy(stacks), lambda x: x)
