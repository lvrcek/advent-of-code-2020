#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 3, Part 1
"""


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    right = 3
    down = 1

    x, y = 0, 0
    end = len(lines)
    length = len(lines[0])
    counter = 0

    while True:
        x = (x + right) % length
        y += down
        if y >= end:
            break
        if lines[y][x] == '#':
            counter += 1

    print(counter)


if __name__ == '__main__':
    main()


