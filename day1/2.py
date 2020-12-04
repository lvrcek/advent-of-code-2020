#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 1, Part 2
"""


def main():

    with open('in.txt') as f:
        numbers = list(map(int, f.readlines()))

    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 2020:
                    print(i * j * k)
                    return


if __name__ == '__main__':
    main()
