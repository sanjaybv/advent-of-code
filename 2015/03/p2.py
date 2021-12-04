import fileinput
from itertools import combinations


class giver:
    def __init__(self, houses):
        self.houses = houses
        self.x, self.y = 0, 0

    def visit(self, moves):
        for move in moves:
            self.houses[(self.x, self.y)] = True
            if move == '^':
                self.y += 1
            elif move == 'v':
                self.y -= 1
            elif move == '>':
                self.x += 1
            else:
                self.x -= 1
        self.houses[(self.x, self.y)] = True

    def num_houses(self):
        return len(self.houses)


if __name__ == "__main__":
    lines = [line.strip() for line in fileinput.input()]
    a = [x for i, x in enumerate(lines[0]) if i%2 == 0]
    b = [x for i, x in enumerate(lines[0]) if i%2 != 0]
    houses = {}
    santa = giver(houses)
    robo = giver(houses)
    santa.visit(a)
    robo.visit(b)

    print(len(houses))
