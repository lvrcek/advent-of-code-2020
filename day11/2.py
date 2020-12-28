#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 11, Part 2
"""

from copy import deepcopy


def first_visible(grid, i, j, ii, jj):
    while True:
        i += ii
        j += jj
        if i not in range(len(grid)):
            return 'L'
        if j not in range(len(grid[0])):
            return 'L'
        if grid[i][j] == '.':
            continue
        if grid[i][j] == '#':
            return '#'
        if grid[i][j] == 'L':
            return 'L'


def print_grid(grid):
    grid = [''.join(row) for row in grid]
    grid = '\n'.join(grid)
    print(f'{grid}\n')


def change_state(grid):
    temp_grid = deepcopy(grid)
    changes = False
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):

            if grid[i][j] == '.':
                continue

            if grid[i][j] == 'L':
                sit = True
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        if first_visible(grid, i, j, ii, jj) == '#':
                            sit = False
                if sit:
                    temp_grid[i][j] = '#'
                    changes = True

            if grid[i][j] == '#':
                occ = 0
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        if ii == 0 and jj == 0:
                            pass
                        elif first_visible(grid, i, j, ii, jj) == '#':
                            occ += 1
                    if occ >= 5:
                        temp_grid[i][j] = 'L'
                        changes = True

    grid = deepcopy(temp_grid)
    return changes, grid


def count_occupied(grid):
    counter = 0
    for line in grid:
        for seat in line:
            if seat == '#':
                counter += 1
    return counter


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    grid = [list('.'*1 + line.strip() + '.'*1) for line in lines]
    dots = [list('.' * len(grid[0]))]
    grid = dots + grid + dots

    while True:
        changes, grid = change_state(grid)
        if not changes:
            break

    print(count_occupied(grid))


if __name__ == '__main__':
    main()
