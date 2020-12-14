#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 14, Part 2
"""

import re
from itertools import combinations


def apply_mask(mask, loc):
    new_loc = ''.join([b if m == '0' else m for m, b in zip(mask, loc)])
    locations = []
    rep = new_loc.count('X')
    tmp = '01' * rep
    combs = set(combinations(tmp, rep))

    for comb in combs:
        i = 0
        location = ''
        for s in new_loc:
            if s != 'X':
                location += s
            else:
                location += comb[i]
                i += 1
        locations.append(location)

    return locations


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
            loc = bin(loc)
            loc = loc[2:].rjust(36, '0')
            locations = apply_mask(mask, loc)
            for loc in locations:
                loc = '0b' + loc
                loc = int(loc, 2)
                mem[loc] = value

    suma = sum(mem.values())
    print(suma)


if __name__ == '__main__':
    main()
