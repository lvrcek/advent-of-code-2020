#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 3, Part 2
"""


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    right_steps = [1, 3, 5, 7, 1]
    down_steps = [1, 1, 1, 1, 2]

    end = len(lines)
    length = len(lines[0])
    multiplied = 1

    for right, down in zip(right_steps, down_steps):
        counter = 0
        x, y = 0, 0

        while True:
            x = (x + right) % length
            y += down
            if y >= end:
                break
            if lines[y][x] == '#':
                counter += 1

        multiplied *= counter

    print(multiplied)


if __name__ == '__main__':
    main()
