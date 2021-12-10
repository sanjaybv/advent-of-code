import fileinput
from os import remove
from typing import List
import math

lines = [line.strip() for line in fileinput.input()]
unique_digits = []
all_digits = []
for line in lines:
    line = line.split('|')
    if len(line) != 2:
        continue
    all_digits.append(line[1].strip().split(" "))
    unique_digits.append(line[0].strip().split(" "))


def unique_counts() -> int:
    count = 0
    for digits in all_digits:
        count += sum(1 for _ in filter(lambda x: x in [2, 3, 4, 7], map(lambda d: len(d), digits)))
    return count

# part 1
print(unique_counts())

def find_len(all_nums, l):
    for n in all_nums:
        if len(n) == l:
            return n
    raise Exception(f'num with len {l} not found in {all_nums}')

def missing(s):
    for c in 'abcdefg':
        if c not in s:
            return c

def missing_all(fr, i):
    out = []
    for c in fr:
        if c not in i:
            out.append(c)
    return out

def make_map(all_nums):
    final = {}

    def add(x, n): 
        final[''.join(sorted(x))] = n

    num_1 = find_len(all_nums, 2)
    add(num_1, 1)


    num_7 = find_len(all_nums, 3)
    add(num_7, 7)

    num_4 = find_len(all_nums, 4)
    add(num_4, 4)

    num_8 = find_len(all_nums, 7)
    add(num_8, 8)

    # find 3
    num_3 = ''
    n_235 = list(filter(lambda n: len(n) == 5, all_nums))
    for nums in n_235:
        if num_1[0] in nums and num_1[1] in nums:
            num_3 = nums
            add(nums, 3)

    left_1 = ''.join(missing_all(num_8, num_3))


    # find 6
    num_6 = ''
    n_069 = list(filter(lambda n: len(n) == 6, all_nums))
    for nums in n_069:
        if missing(nums) in num_1:
            num_6 = nums
            add(nums, 6)
        elif missing(nums) in left_1:
            add(nums, 9)
        else:
            add(nums, 0)

    for num in n_235:
        if num == num_3:
            continue
        if len(missing_all(num_6, num)) == 1:
            add(num, 5)
        else:
            add(num, 2)

    return final



def num(digits: List[int]) -> int:
    n = 0
    for i, d in enumerate(reversed(digits)):
        n += math.pow(10, i)*d
    return n
        


def total() -> int:
    t = 0
    for unique, digits in zip(unique_digits, all_digits):
        m = make_map(unique)
        t += num(list(map(lambda d: m[''.join(sorted(d))], digits)))
    return int(t)

print(total())
