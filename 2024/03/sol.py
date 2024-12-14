import fileinput
import re

regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
regex_d = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))")

lines = [l.strip() for l in fileinput.input()]

total = 0
for l in lines:
    groups = regex.findall(l)
    total += sum([int(a) * int(b) for a, b in groups])
print(total)

total = 0
enabled = True
for l in lines:
    for g in regex_d.findall(l):
        if g[3]:
            enabled = False
        elif g[2]:
            enabled = True
        elif enabled:
            total += int(g[0]) * int(g[1])
        # print(g, bool(g[3]), total)
print(total)
