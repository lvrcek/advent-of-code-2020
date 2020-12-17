#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 17, Part 2
"""

from copy import deepcopy


def print_grid(grid):
    grid = [' '.join(map(str, row)) for row in grid]
    grid = '\n'.join(grid)
    print(f'{grid}\n')


def print_space(space):
    for i, s in enumerate(space):
        print('layer:', i)
        print_grid(s)


def count_active(hyper):
    counter = 0
    for space in hyper:
        for layer in space:
            for row in layer:
                for n in row:
                    counter += n
    return counter


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    grid = []
    N = 6

    for line in lines:
        row = [0 for _ in range(N+1)] + [0 if c == '.' else 1 for c in line.strip()] + [0 for _ in range(N+1)]
        grid.append(row)

    dots = [0 for _ in grid[0]]
    grid = [deepcopy(dots) for _ in range(N+1)] + deepcopy(grid) + [deepcopy(dots) for _ in range(N+1)]
    dot_grid = [deepcopy(dots) for _ in grid]
    spac = [deepcopy(dot_grid) for _ in range(N+1)] + deepcopy([grid]) + [deepcopy(dot_grid) for _ in range(N+1)]
    dot_spac = [deepcopy(dot_grid) for _ in spac]
    hyper = [deepcopy(dot_spac) for _ in range(N+1)] + deepcopy([spac]) + [deepcopy(dot_spac) for _ in range(N+1)]

    dim = len(hyper)
    height = len(hyper[0])
    rows = len(hyper[0][0])
    columns = len(hyper[0][0][0])

    for n in range(1, N+1):
        new_hyper = deepcopy(hyper)
        for w in range(1, dim-1):
            for k in range(1, height-1):
                for i in range(1, rows-1):
                    for j in range(1, columns-1):

                        count = 0
                        for ww in range(w-1, w+2):
                            for kk in range(k-1, k+2):
                                for ii in range(i-1, i+2):
                                    for jj in range(j-1, j+2):
                                        if ii == i and jj == j and kk == k and ww == w:
                                            continue
                                        count += hyper[ww][kk][ii][jj]

                        if (hyper[w][k][i][j] == 0 and count == 3) or (hyper[w][k][i][j] == 1 and count in (2,3)):
                            new_hyper[w][k][i][j] = 1
                        else:
                            new_hyper[w][k][i][j] = 0

        hyper = deepcopy(new_hyper)
        print('FINISHED ROUND:', n)

    total = count_active(hyper)
    print(total)


if __name__ == '__main__':
    main()
