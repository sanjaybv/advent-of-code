import re
import numpy as np

line = input()
nums = np.array([int(x) for x in re.findall(r'\d+', line)])

nums.sort()


def calc(f) -> int:
    min_fuel = 0
    for i in range (nums[0], nums[-1]+1):
        cur = f(i)
        if min_fuel == 0 or cur < min_fuel:
            min_fuel = cur
    return min_fuel
    
# part 1
print(calc(lambda i: np.sum(np.abs(nums-i))))

# part 2
print(calc(lambda i: np.sum(list(map(lambda n: n*(n+1)/2, np.abs(nums-i))))))
