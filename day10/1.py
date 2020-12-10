#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 10, Part 1
"""


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    numbers = list(map(int, lines))
    numbers = [0] + sorted(numbers) + [max(numbers) + 3]

    diff = [m-n for n, m in zip(numbers[:-1], numbers[1:])]
    sol = diff.count(1) * diff.count(3)
    print(sol)


if __name__ == '__main__':
    main()
