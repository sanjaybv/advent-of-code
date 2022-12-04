import fileinput

def priority(ch):
    if ch.isupper():
        return ord(ch) - ord('A') + 27
    else:
        return ord(ch) - ord('a') + 1


lines = [x.strip() for x in fileinput.input()]

# part 1
ps = 0
for line in lines:
    ch = next(iter(set(line[:int(len(line)/2)]) & set(line[int(len(line)/2):])))
    ps += priority(ch)

print(ps)


# part 2
ps = 0
for i in range(0, len(lines), 3):
    ch = next(iter(set(lines[i]) & set(lines[i+1]) & set(lines[i+2])))
    ps += priority(ch)

print(ps)
