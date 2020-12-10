#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 2, Part 1
"""


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    counter = 0

    for line in lines:
        policy, c, password = line.strip().split()
        c = c[:-1]
        low, high = map(int, policy.split('-'))
        number = password.count(c)
        if low <= number <= high:
            counter += 1

    print(counter)


if __name__ == '__main__':
    main()
