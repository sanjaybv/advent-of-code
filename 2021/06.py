import re
from typing import Counter

line = input()
nums = [int(x) for x in re.findall(r'\d+', line)]



def sim(n):
    counts = [0] * 9
    c = Counter(nums)
    for i in range(8):
        counts[i] = c[i]

    for d in range(n):
        counts.append(counts[0])
        counts[7] += counts[0]
        counts = counts[1:]

    return sum(counts)


print(sim(80))
print(sim(256))
