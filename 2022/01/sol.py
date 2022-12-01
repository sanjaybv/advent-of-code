import fileinput

cals = []
local_sum = 0
for line in fileinput.input():
    if line != "\n":
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
