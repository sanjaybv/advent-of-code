with open('input.txt') as input_file:
    input_text = input_file.read()

instructions = input_text.strip().split(', ')

#  0
# 3 1
#  2
direction = 0
x, y = 0, 0
for step in instructions:
    turn = step[0]
    count = int(step[1:])
    
    if turn == 'R':
        direction += 1
    else:
        direction -= 1
    direction %= 4

    if direction == 0:
        y += count
    elif direction == 1:
        x += count
    elif direction == 2:
        y -= count
    else:
        x -= count

    print step, abs(x) + abs(y)
