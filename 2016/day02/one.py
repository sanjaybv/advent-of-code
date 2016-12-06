with open('input.txt') as input_file:
    input_lines = [line.strip() for line in input_file]


keypad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
pos = [1, 1]
code = ''
for line in input_lines:
    for step in line:
        if step == 'U':
            pos[0] -= 1 if pos[0] > 0 else 0
        elif step == 'R':
            pos[1] += 1 if pos[1] < 2 else 0
        elif step == 'D':
            pos[0] += 1 if pos[0] < 2 else 0
        else:
            pos[1] -= 1 if pos[1] > 0 else 0
        print step, pos

    code += str(keypad[pos[0]][pos[1]])

print code
