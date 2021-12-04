import fileinput

def increases(numbers):
    return [num > prev for prev, num in zip(numbers, numbers[1:])].count(True)

numbers = [int(line.strip()) for line in fileinput.input()]

# part 1
print(increases(numbers))

# part 2
sums = [sum(x) for x in zip(numbers, numbers[1:], numbers[2:])]
print(increases(sums))
