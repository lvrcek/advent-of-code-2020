#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 1, Part 1
"""


def main():

    with open('in.txt') as f:
        numbers = list(map(int, f.readlines()))

    for i in numbers:
        for j in numbers:
            if i + j == 2020:
                print(i * j)
                return


if __name__ == '__main__':
    main()
