import fileinput

lines = [l.strip() for l in fileinput.input()]

def sections(line: str) -> tuple:
    ass = line.split(',')
    e1 = list(map(int, ass[0].split('-')))
    e2 = list(map(int, ass[1].split('-')))
    return set(range(e1[0], e1[1]+1)), set(range(e2[0], e2[1]+1))


# part 1
print(sum(map(lambda s: s[0] <= s[1] or s[1] <= s[0], (sections(l) for l in lines))))
# part 2
print(sum(map(lambda s: len(s[0] & s[1]) > 0, (sections(l) for l in lines))))
