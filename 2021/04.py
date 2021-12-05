import fileinput
import numpy as np
from typing import List, Tuple

class Bingo(object):
    def __init__(self, board) -> None:
        super().__init__()
        self.board = np.array(board)
        self.win = False
        self.marks: np.ndarray = np.zeros((5, 5))

    def mark(self, num: int) -> Tuple[int, int]:
        for i, row in enumerate(self.board):
            for j, item in enumerate(row):
                if item == num:
                    self.marks[i][j] = 1
                    return i, j
        return None

    def is_win(self, pos: Tuple[int, int]) -> bool:
        if self.win:
            return True
        if not pos:
            return False
        if self.marks.sum(axis=1)[pos[0]] == 5:
            self.win = True
            return True
        if self.marks.sum(axis=0)[pos[1]] == 5:
            self.win = True
            return True
        return False

    def sum_unmarked(self) -> int:
        return np.multiply(
            self.board, 
            np.multiply(np.add(self.marks, -1), -1)
        ).sum()


def main():
    boards: List[Bingo] = []
    numbers = []

    cur_board_lines = []
    for line in fileinput.input():
        line = line.strip()
        if not numbers:
            numbers = [int(x) for x in line.split(',')]
            continue
        if line == "":
            continue
        cur_board_lines.append([int(x) for x in filter(lambda n: n != "", line.split(" "))])
        if len(cur_board_lines) == 5:
            boards.append(Bingo(cur_board_lines))
            cur_board_lines = []

    for n in numbers:
        for i, b in enumerate(boards):
            if b.is_win(None):
                continue
            if b.is_win(b.mark(n)):
                print(n * b.sum_unmarked())

if __name__ == "__main__":
    main()
