import fileinput

nums = [list(map(lambda x: int(x), list(line.strip()))) for line in fileinput.input()]

def at(nums, i, j):
    if i < 0 or i >= len(nums) or j < 0 or j >= len(nums[0]):
        return None
    return nums[i][j]

def neighbors(nums, i, j):
    neighs = [
        (at(nums, i-1, j), (i-1, j)),
        (at(nums, i+1, j), (i+1, j)),
        (at(nums, i, j-1), (i, j-1)),
        (at(nums, i, j+1), (i, j+1)),
    ]
    for n, pos in neighs:
        if n != None:
            yield pos

def risk_level(nums, i, j):
    trues = 4
    for x, y in neighbors(nums, i, j):
        # print(x, y)
        if nums[x][y] <= nums[i][j]:
            trues -= 1
    # print("for", i, j, trues, nums[i][j])
    return 1+nums[i][j] if trues == 4 else 0

total_risk = 0
for i in range(len(nums)):
    for j in range(len(nums[i])):
        total_risk += risk_level(nums, i, j)

print(total_risk)


def key(i, j):
    return '{0},{1}'.format(i, j)

def add_key(s, i, j):
    s.update({key(i, j)})

seen = set()
def basin_at(nums, i, j):
    global seen
    if key(i, j) in seen:
        return 0

    st = [(i, j)]
    add_key(seen, i, j)
    seen_now = 0
    while st:
        cur_i, cur_j = st.pop()
        for x, y in neighbors(nums, cur_i, cur_j):
            if nums[x][y] != 9 and key(x, y) not in seen:
                st.append((x, y))
                seen_now += 1
                add_key(seen, x, y)
    return seen_now


basins = [basin_at(nums, i, j) for j in range(len(nums[i])) for i in range(len(nums))]
basins.sort()

print(basins[-1]*basins[-2]*basins[-3])
