#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 17, Part 1
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


def count_active(space):
    counter = 0
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
    grid = [deepcopy(dots) for _ in range(N+1)] + grid + [deepcopy(dots) for _ in range(N+1)]
    dot_grid = [deepcopy(dots) for _ in grid]
    space = [deepcopy(dot_grid) for _ in range(N+1)] + [grid] + [deepcopy(dot_grid) for _ in range(N+1)]

    height = len(space)
    rows = len(space[0])
    columns = len(space[0][0])

    for n in range(1, N+1):
        new_space = deepcopy(space)

        for k in range(1, height-1):
            for i in range(1, rows-1):
                for j in range(1, columns-1):

                    count = 0

                    for kk in range(k-1, k+2):
                        for ii in range(i-1, i+2):
                            for jj in range(j-1, j+2):
                                if ii == i and jj == j and kk == k:
                                    continue
                                count += space[kk][ii][jj]

                    if (space[k][i][j] == 0 and count == 3) or (space[k][i][j] == 1 and count in (2,3)):
                        new_space[k][i][j] = 1
                    else:
                        new_space[k][i][j] = 0

        space = deepcopy(new_space)
        # print('FINISHED ROUND:', n)

    total = count_active(space)
    print(total)


if __name__ == '__main__':
    main()
