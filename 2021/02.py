import fileinput
import numpy

commands = [(a, int(b)) for a, b in [line.strip().split(" ") for line in fileinput.input()]]


def simple(commands): 
    horiz, depth = 0, 0
    for action, arg in commands:
        if action == "forward":
            horiz += arg
        elif action == "up":
            depth -= arg
        elif action == "down":
            depth += arg
        else:
            raise Exception(f"invalid action {action}")
    return horiz, depth

def with_aim(commands): 
    horiz, depth, aim = 0, 0, 0
    for action, arg in commands:
        if action == "forward":
            horiz += arg
            depth += aim * arg
        elif action == "up":
            aim -= arg
        elif action == "down":
            aim += arg
        else:
            raise Exception(f"invalid action {action}")
    return horiz, depth

# part 1
print(numpy.prod(simple(commands)))

# part 2
print(numpy.prod(with_aim(commands)))
