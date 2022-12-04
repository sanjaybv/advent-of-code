import fileinput

lines = [x.strip() for x in fileinput.input()]

# part a
# wins is a directed graph with scores as the values
wins = {
        'A': {'X': 3, 'Y': 6, 'Z': 0},
        'B': {'X': 0, 'Y': 3, 'Z': 6},
        'C': {'X': 6, 'Y': 0, 'Z': 3},
       }
shape_score = {'X': 1, 'Y': 2, 'Z': 3}

score = 0
for line in lines:
    them, me = line.split(' ')
    score += wins[them][me] + shape_score[me]
print(score)


# part b
wins = {
        'A': {'X': 3, 'Y': 1, 'Z': 2},
        'B': {'X': 1, 'Y': 2, 'Z': 3},
        'C': {'X': 2, 'Y': 3, 'Z': 1},
       }
result_score = {'X': 0, 'Y': 3, 'Z': 6}

score = 0
for line in lines:
    them, me = line.split(' ')
    score += wins[them][me] + result_score[me]
print(score)
