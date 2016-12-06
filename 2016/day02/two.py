with open('input.txt') as input_file:
    input_lines = [line.strip() for line in input_file]

keypad = ['00100',
          '02340',
          '56789',
          '0ABC0',
          '00D00']
pos = [1, 1]

def get_key():
    return keypad[pos[0]][pos[1]]

code = ''
for line in input_lines:
    for step in line:
        if step == 'U':
            pos[0] -= 1 if get_key() not in '52149' else 0
        elif step == 'R':
            pos[1] += 1 if get_key() not in 'CD149' else 0
        elif step == 'D':
            pos[0] += 1 if get_key() not in '9CD5A' else 0
        else:
            pos[1] -= 1 if get_key() not in '125AD' else 0

    code += get_key()

print code
