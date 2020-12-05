#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 5, Part 1
"""


def convert_row(row):
    bin_row = '0b' + ''.join(['0' if c == 'F' else '1' for c in row])
    return int(bin_row, 2)


def convert_col(col):
    bin_col = '0b' + ''.join(['0' if c == 'L' else '1' for c in col])
    return int(bin_col, 2)


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    id_list = []

    for line in lines:
        line = line.strip()
        row, col = line[:-3], line[-3:]
        row = convert_row(row)
        col = convert_col(col)
        id_list.append(row * 8 + col)

    print(max(id_list))


if __name__ == '__main__':
    main()
