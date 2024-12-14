import fileinput
from functools import cmp_to_key

type Orders = dict[str, set[str]]

def graph(lines: list[str]) -> Orders:
    ret: Orders = {}
    for l in lines:
        parts = l.split('|')
        ret.setdefault(parts[0], set()).add(parts[1])
    return ret

def is_ordered(nums: list[str], orders: Orders) -> bool:
    for i, n in enumerate(nums[:-1]):
        if n not in orders or not all([next in orders[n] for next in nums[i+1:]]):
            return False
    return True


def ordered_total(lines: list[str], orders: Orders) -> tuple[int, int]:
    total_ord = 0
    total_unord = 0
    for l in lines:
        nums = l.split(',')
        if is_ordered(nums, orders):
            total_ord += int(nums[int(len(nums)/2)])
        else:
            total_unord +=int(order_updates(nums, orders)[int(len(nums)/2)])
    return (total_ord, total_unord)

def order_updates(nums: list[str], orders: Orders) -> list[str]:
    nums.sort(key=cmp_to_key(lambda a, b: -1 if b in orders[a] else 1))
    return nums

lines = [l.strip() for l in fileinput.input()]
sep = lines.index('')

orders = graph(lines[:sep])

print(ordered_total(lines[sep+1:], orders))

