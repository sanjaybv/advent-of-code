import fileinput
import numpy as np

lines = [line.strip() for line in fileinput.input()]

openers = { '{': '}', '(': ')', '[': ']', '<': '>'}
closers = { '}': '{', ')': '(', ']': '[', '>': '<'}
points = { '}': 1197, ')': 3, ']': 57, '>': 25137}
imcomp_points = { '{': 3, '(': 1, '[': 2, '<': 4}

illegals = {}
corrupted_points = 0
incomplete_points = []
for line in lines:
    st = []
    for ch in line:
        if ch in openers:
            st.append(ch)
        else:
            if len(st) == 0:
                break
            if closers[ch] == st[-1]:
                st.pop()
            else:
                illegals[ch] = illegals[ch] + 1 if ch in illegals else 1
                corrupted_points += points[ch]
                break
    else:
        p = 0
        while st:
            p = 5*p + imcomp_points[st.pop()]
        incomplete_points.append(p)



print(corrupted_points)
print(int(np.median(incomplete_points)))
