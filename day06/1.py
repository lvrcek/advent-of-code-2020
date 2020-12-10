#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 6, Part 1
"""


def main():
    with open('in.txt') as f:
        lines = f.read().split('\n\n')

    total = 0
    for group in lines:
        unique = set(group)
        total += len(unique) if '\n' not in unique else len(unique) - 1

    print(total)


if __name__ == '__main__':
    main()
