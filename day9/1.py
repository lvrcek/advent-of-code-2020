#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 9, Part 1
"""


def find_sums(numbers):
    return [n + m for n in numbers for m in numbers]


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    numbers = list(map(int, lines))
    for i, number in enumerate(numbers):
        if i < 25:
            continue
        sums = find_sums(numbers[i-25:i])
        if number not in sums:
            print(number)
            break


if __name__ == '__main__':
    main()
