import fileinput
import copy

lines = [l.rstrip('\n') for l in fileinput.input()]

init_lines = lines[:lines.index('')]

stacks = []


nums = list(map(int, init_lines[-1].split()))

col = 0
for col in range(len(init_lines[-1])):
    if not init_lines[-1][col].isnumeric():
        continue
    row = len(init_lines) - 2
    s =  []
    while row >= 0 and init_lines[row][col].isalpha():
        s.append(init_lines[row][col])
        row -= 1
    stacks.append(s)

stacks_1 = copy.deepcopy(stacks)

for line in lines[lines.index('')+1:]:
    it = map(int, filter(lambda x: x.isnumeric(), line.split()))
    a = next(it)
    f = next(it) - 1
    t = next(it) - 1

    for i in range(a):
        stacks_1[t].append(stacks_1[f].pop())

print(''.join([s.pop() for s in stacks_1]))

stacks_2 = copy.deepcopy(stacks)
for line in lines[lines.index('')+1:]:
    it = map(int, filter(lambda x: x.isnumeric(), line.split()))
    a = next(it)
    f = next(it) - 1
    t = next(it) - 1

    stacks_2[t].extend(stacks_2[f][-a:])
    stacks_2[f] = stacks_2[f][:-a]

print(''.join([s.pop() for s in stacks_2]))

