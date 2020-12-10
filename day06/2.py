#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 6, Part 2
"""

import string


def main():
    with open('in.txt') as f:
        lines = f.read().split('\n\n')

    letters = string.ascii_lowercase

    total = 0
    questions = set(list(letters))
    for group in lines:

        for line in group.split('\n'):
            questions &= set(list(line))

        total += len(questions)
        questions = set(list(letters))

    print(total)


if __name__ == '__main__':
    main()
