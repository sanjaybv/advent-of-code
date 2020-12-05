import fileinput
import re

matcher = re.compile(r'^([-\d]+)-([-\d]+) ([a-z]): (\w+)')

lines = [line.strip() for line in fileinput.input()]
parsed_lines = []
for line in lines:
    result = matcher.match(line)
    parsed_lines.append(result.groups())

num_valid = 0
for l in parsed_lines:
    min_val = int(l[0])
    max_val = int(l[1])
    char = l[2]
    pwd = l[3]

    count = pwd.count(char)
    if count >= min_val and count <= max_val:
        num_valid += 1

print(num_valid)

num_valid = 0
for l in parsed_lines:
    idx_1 = int(l[0])
    idx_2 = int(l[1])
    char = l[2]
    pwd = l[3]

    if pwd[idx_1-1] == char and pwd[idx_2-1] != char or pwd[idx_1-1] != char and pwd[idx_2-1] == char:
        num_valid += 1

print(num_valid)
