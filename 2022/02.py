from aocd import get_data

wins = {
        'A': {'X': 3, 'Y': 6, 'Z': 0},
        'B': {'X': 0, 'Y': 3, 'Z': 6},
        'C': {'X': 6, 'Y': 0, 'Z': 3},
       }

shape_score = {'X': 1, 'Y': 2, 'Z': 3}

score = 0
s = 0
for line in get_data(year=2022, day=2).split('\n'):
    shapes = line.split(' ')
    them = ord(shapes[0]) - ord('A')
    me = ord(shapes[1]) - ord('X')
    d = (me - them) % 3
    if d == 0:
        s += 3
    elif d == 1:
        s += 6
    s += me + 1
    score += wins[shapes[0]][shapes[1]] + shape_score[shapes[1]]

print(score)
print(s)

result_score = {'X': 0, 'Y': 3, 'Z': 6}

wins = {
        'A': {'X': 3, 'Y': 1, 'Z': 2},
        'B': {'X': 1, 'Y': 2, 'Z': 3},
        'C': {'X': 2, 'Y': 3, 'Z': 1},
       }

score = 0
for line in get_data(year=2022, day=2).split('\n'):
    shapes = line.split(' ')
    score += wins[shapes[0]][shapes[1]] + result_score[shapes[1]]
print(score)
