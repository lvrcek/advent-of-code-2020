#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 10, Part 2
"""


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    numbers = list(map(int, lines))
    numbers = [0] + sorted(numbers) + [max(numbers) + 3]

    paths_count = [0 for _ in numbers]
    paths_count[0] = 1

    for i in range(len(numbers)):
        if i == 0:
            paths_count[i] = 1
            continue
        for j in range(i-1, max(i-4, -1), -1):
            if numbers[i] - numbers[j] <= 3:
                paths_count[i] += paths_count[j]

    print(paths_count[-1])


if __name__ == '__main__':
    main()
