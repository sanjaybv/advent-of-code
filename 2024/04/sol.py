import fileinput
from collections import Counter

lines = [l.strip() for l in fileinput.input()]
n_rows = len(lines)
n_cols = len(lines[0])

def search_xmas(i: int, j: int) -> int:
    # add all the word patterns
    words = []
    if j+3 < n_cols:
        words.append(lines[i][j]+lines[i][j+1]+lines[i][j+2]+lines[i][j+3])
    if j > 2:
        words.append(lines[i][j]+lines[i][j-1]+lines[i][j-2]+lines[i][j-3])
    if i+3 < n_rows:
        words.append(lines[i][j]+lines[i+1][j]+lines[i+2][j]+lines[i+3][j])
    if i > 2:
        words.append(lines[i][j]+lines[i-1][j]+lines[i-2][j]+lines[i-3][j])
    if j+3 < n_cols and i+3 < n_rows:
        words.append(lines[i][j]+lines[i+1][j+1]+lines[i+2][j+2]+lines[i+3][j+3])
    if j+3 < n_cols and i > 2:
        words.append(lines[i][j]+lines[i-1][j+1]+lines[i-2][j+2]+lines[i-3][j+3])
    if j > 2 and i+3 < n_rows:
        words.append(lines[i][j]+lines[i+1][j-1]+lines[i+2][j-2]+lines[i+3][j-3])
    if j > 2 and i > 2:
        words.append(lines[i][j]+lines[i-1][j-1]+lines[i-2][j-2]+lines[i-3][j-3])

    return Counter(words)['XMAS']

def search_mas(i: int, j: int) -> int:
    a = lines[i-1][j-1]+lines[i][j]+lines[i+1][j+1]
    b = lines[i-1][j+1]+lines[i][j]+lines[i+1][j-1]
    print(a, b)
    if (a == 'MAS' or a == 'SAM') and (b == 'MAS' or b == 'SAM'):
        return 1
    return 0

count_xmas = 0
for i, row in enumerate(lines):
    for j, ch in enumerate(row):
        count_xmas += search_xmas(i, j)
print(count_xmas)

count_mas = 0
for i in range(1, n_rows-1):
    for j in range(1, n_cols-1):
        count_mas += search_mas(i, j)
print(count_mas)
