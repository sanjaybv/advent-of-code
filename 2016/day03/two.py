count = 0

def transpose(nums):
    nums[0][1], nums[1][0] = nums[1][0], nums[0][1]
    nums[0][2], nums[2][0] = nums[2][0], nums[0][2]
    nums[1][2], nums[2][1] = nums[2][1], nums[1][2]

numbers = []
with open('input.txt') as input_file:
    for i, line in enumerate(input_file):
        numbers.append(map(int, line.strip().split()))
        if i % 3 == 2:
            transpose(numbers)
            for nums in numbers:
                if nums[0] < nums[1] + nums[2] and\
                        nums[1] < nums[0] + nums[2] and\
                        nums[2] < nums[0] + nums[1]:
                    count += 1
            numbers = []

print count
