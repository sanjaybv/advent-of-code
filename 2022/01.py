from aocd import get_data

cals = []
local_sum = 0
for line in get_data(year=2022, day=1).split('\n'):
    if line != "":
       local_sum += int(line)
    else:
        cals.append(local_sum)
        local_sum = 0

cals.append(local_sum)
cals.sort()

# part 1
print(cals[-1])

# part 2
print(sum(cals[-3:]))

