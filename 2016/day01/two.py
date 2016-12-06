with open('input.txt') as input_file:
    input_text = input_file.read()

instructions = input_text.strip().split(', ')

#  0
# 3 1
#  2
direction = 0
x, y = 0, 0
visited = set([(0, 0)])
for step in instructions:
    turn = step[0]
    count = int(step[1:])
    
    if turn == 'R':
        direction += 1
    else:
        direction -= 1
    direction %= 4

    while count:
        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        else:
            x -= 1
        count -= 1

        if (x, y) in visited:
            break
        visited.add((x, y))
    else:
        continue

    break

print abs(x) + abs(y)
