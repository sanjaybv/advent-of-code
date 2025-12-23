import fileinput
import numpy as np

turn = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^',
}

m = np.array([list(l.strip()) for l in fileinput.input()])

def move_to(a:int, b:int, x: int, y: int, dir: str) -> bool:
    if x < 0 or x >= m.shape[0]:
        m[a, b] = 'X'
        return False
    if y < 0 or y >= m.shape[1]:
        m[a, b] = 'X'
        return False

    if m[x,y] == '#':
        m[a,b] = turn[dir]
        return True

    m[a, b] = 'X'
    m[x, y] = dir
    return True

def tick() -> bool:
    x, y = np.where(np.isin(m, list(turn.keys())))
    pos = (x[0], y[0])
    dir = str(m[pos[0], pos[1]])

    cont = True
    if dir == '^':
        cont = move_to(pos[0], pos[1], pos[0]-1, pos[1], str(dir))
    if dir == '>':
        cont = move_to(pos[0], pos[1], pos[0], pos[1]+1, dir)
    if dir == 'v':
        cont = move_to(pos[0], pos[1], pos[0]+1, pos[1], dir)
    if dir == '<':
        cont = move_to(pos[0], pos[1], pos[0], pos[1]-1, dir)

    return cont


while tick():
    pass

print(np.count_nonzero(m == 'X'))
