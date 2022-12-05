import fileinput

lines = [l.strip() for l in fileinput.input()]

def sections(line: str) -> tuple:
    ass = line.split(',')
    e1 = list(map(int, ass[0].split('-')))
    e2 = list(map(int, ass[1].split('-')))
    return set(range(e1[0], e1[1]+1)), set(range(e2[0], e2[1]+1))

# part 1
c = 0
for l in lines:
    s1, s2 = sections(l)
    if s1 <= s2 or s2 <= s1:
        c += 1

print(c)


# part 2
c = 0
for l in lines:
    s1, s2 = sections(l)
    if len(s1 & s2) > 0:
        c += 1

print(c)
