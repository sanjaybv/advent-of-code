import fileinput
from itertools import tee
from copy import deepcopy as dcopy

lines = [l.rstrip('\n') for l in fileinput.input()]

sl = lines[:lines.index('')]
stacks = []
for col in range(1, len(sl[-1]), 4):
    stacks.append(list(filter(str.isalpha, map(
        lambda row: sl[row][col], range(len(sl) - 2, -1, -1)
    ))))


ins =  map(
            lambda parts: map(
                lambda x: int(x[1]) if x[0] < 1 else int(x[1])-1, enumerate(filter(str.isnumeric, parts))
            ), (l.split() for l in lines[lines.index('')+1:])
       )
ia, ib = tee(ins)

def solve(ins, s, func):
    for i in ins:
        a, f, t = list(i)
        s[t].extend(func(s[f][-a:]))
        s[f] = s[f][:-a]
    print(''.join([j.pop() for j in s]))

# part 1
solve(ia, dcopy(stacks), reversed)

# part 2
solve(ia, dcopy(stacks), lambda x: x)
