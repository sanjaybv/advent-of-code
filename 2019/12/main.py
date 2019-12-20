from fileinput import input as f_input
import re
from itertools import permutations

class Moon:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        self.vel = [0, 0, 0]

    def gravitate(self, neighbor):
        for i, v in enumerate(self.pos):
            if v < neighbor.pos[i]:
                self.vel[i] += 1
            elif v > neighbor.pos[i]:
                self.vel[i] -= 1

    def velocitate(self):
        self.pos = [self.pos[i] + v for i, v in enumerate(self.vel)]

    def energy(self):
        return sum(map(abs, self.pos)) * sum(map(abs, self.vel))


def main():
    moons = []
    matcher = re.compile(r'^<x=([-\d]+), y=([-\d]+), z=([-\d]+)>$')
    for line in f_input():
        result = matcher.match(line)
        moons.append(Moon(*map(int, result.groups())))

    for t in range(1000):
        for a, b in permutations(moons, 2):
            a.gravitate(b)

        for m in moons:
            m.velocitate()

    print(sum(m.energy() for m in moons))

if __name__ == "__main__":
    main()
