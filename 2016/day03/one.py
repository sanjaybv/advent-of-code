count = 0

with open('input.txt') as input_file:
    for line in input_file:
        nums = map(int, line.strip().split())
        print nums
        if nums[0] < nums[1] + nums[2] and\
                nums[1] < nums[0] + nums[2] and\
                nums[2] < nums[0] + nums[1]:
            count += 1

print count
