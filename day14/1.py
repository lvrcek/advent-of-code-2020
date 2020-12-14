#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 14, Part 1
"""

import re


def apply_mask(mask, value):
    return ''.join([b if m == 'X' else m for m, b in zip(mask, value)])


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    mem = {}
    pattern = r'mem\[(\d*)\] = (\d*)'
    for line in lines:
        if 'mask' in line:
            mask = line.strip().split()[-1]
        else:
            loc, value = map(int, re.findall(pattern, line.strip())[0])
            value = bin(value)
            value = value[2:].rjust(36, '0')
            value = '0b' + apply_mask(mask, value)
            mem[loc] = int(value, 2)

    suma = sum(mem.values())
    print(suma)


if __name__ == '__main__':
    main()
