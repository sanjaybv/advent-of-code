import fileinput

lines = [line for line in fileinput.input()].join('\n')

cals = sorted((sum(map(int, items.split())) for items in lines.split("\n\n")))

# part 1
print(cals[-1])

# part 2
print(sum(cals[-3:]))

