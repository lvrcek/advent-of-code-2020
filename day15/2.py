#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 15, Part 2
"""


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    numbers = list(map(int, lines[0].strip().split(',')))
    occurrence = {}
    i = 0
    threshold = 30000000

    while True:
        if i < len(numbers):
            new_number = numbers[i]
            if i > 0:
                occurrence[last_number] = i - 1

        else:
            if last_number in occurrence.keys():
                new_number = i - 1 - occurrence[last_number]
            else:
                new_number = 0
            occurrence[last_number] = i - 1

        last_number = new_number
        i += 1

        if i == threshold:
            print(last_number)
            break


if __name__ == '__main__':
    main()
