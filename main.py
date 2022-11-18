#!/usr/bin/env python3

import sys

SIZE = 3

class sudoku:
    def __init__(self):
        self.cells = [[0 for _ in range(SIZE*SIZE)] for _ in range(SIZE*SIZE)]

    def input(self):
        raw = []
        try:
            while True:
                line = input()
                line = line.split()
                raw+=line
        except EOFError:
            pass
        for row in range(SIZE*SIZE):
            for col in range(SIZE*SIZE):
                try:
                    self.cells[row][col] = int(raw[row*SIZE*SIZE+col])
                except ValueError:
                    self.cells[row][col] = -1
                if self.cells[row][col] >= SIZE*SIZE:
                    raise ValueError('Too large input cell.')

    def print(self, ost=sys.stdout):
        for row in range(SIZE*SIZE):
            for col in range(SIZE*SIZE):
                if self.cells[row][col] == -1:
                    print('  ', file=ost, end='')
                else:
                    print(f'{self.cells[row][col]:1} ', file=ost, end='')
            print('', file=ost)
        print('', file=ost)

    def get_first_blank(self):
        for row in range(SIZE*SIZE):
            for col in range(SIZE*SIZE):
                if self.cells[row][col] == -1:
                    return row, col
        return None

    def get_candidates(self, row, col):
        hist = {i:0 for i in range(-1, SIZE*SIZE)}
        for i in range(SIZE*SIZE):
            hist[self.cells[row][i]] += 1
            hist[self.cells[i][col]] += 1
        b_row = row//SIZE
        b_col = col//SIZE
        for i in range(SIZE):
            for j in range(SIZE):
                hist[self.cells[b_row*SIZE+i][b_col*SIZE+j]] += 1
        return [i for i in range(SIZE*SIZE) if hist[i] == 0]

    def dfs(self):
        blank = self.get_first_blank()
        if not blank:
            return True
        row, col = blank
        cands = self.get_candidates(row, col)
        for num in cands:
            self.cells[row][col] = num
            if self.dfs():
                return True
            self.cells[row][col] = -1
        return False

def main():
    sdk = sudoku()
    sdk.input()
    sdk.print()
    sdk.dfs()
    sdk.print()

if __name__ == '__main__':
    main()
