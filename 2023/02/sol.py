import fileinput
from typing import List


lines = [li.strip() for li in fileinput.input()]


def check_reports(levels: List, dir: int) -> bool:
    if len(levels) < 2:
        return True

    diff = levels[1] - levels[0]

    if diff != 0:
        if dir == 0:
            dir = diff / abs(diff)
        if 0 < abs(diff) < 4 and dir == diff / abs(diff):
            return check_reports(levels[1:], dir)

    return False


def to_ints(li):
    return [int(s) for s in li.split(" ")]


print([check_reports(to_ints(l), 0) for l in lines].count(True))

results = []
for l in lines:
    levels = to_ints(l)
    if check_reports(levels, 0):
        results.append(True)
    else:
        for i in range(len(levels)):
            if check_reports(levels[:i] + levels[i + 1 :], 0):
                results.append(True)
                break
            results.append(False)
print(results.count(True))
