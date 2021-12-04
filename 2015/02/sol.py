import fileinput
from itertools import combinations

lines = [line.strip() for line in fileinput.input()]
numbers = []
total = 0
ribbon = 0
for line in lines:
    nums = [int(x) for x in line.split('x')]
    nums.sort()
    for comb in combinations(nums, 2):
        total += 2 * comb[0] * comb[1]
    total += nums[0] * nums[1]
    ribbon += 2*nums[0] + 2*nums[1] + nums[0]*nums[1]*nums[2]

print(total)
print(ribbon)

