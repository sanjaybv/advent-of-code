import fileinput
import numpy as np
from collections import Counter

lines = [line.strip().split("   ") for line in fileinput.input()]

nums = np.array(lines).transpose()
l1 = np.sort(list([int(n) for n in nums[0]]))
l2 = np.sort(list([int(n) for n in nums[1]]))

counts = dict(Counter(l2))

print(sum([abs(a - b) for a, b in zip(l1, l2)]))
print(sum([a * counts.get(a, 0) for a in l1]))
