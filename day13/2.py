#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 13, Part 2
"""


def main():
    with open('in.txt') as f:
        lines = f.readlines()
    arrival = int(lines[0].strip())
    bus_ids = []
    for i, n in enumerate(lines[1].strip().split(',')):
        if n == 'x':
            continue
        else:
            # Set the remainders to be in range [0, n)
            bus_ids.append(((int(n) - i) % int(n), int(n)))

    bus_sorted = sorted(bus_ids, key=lambda x: -x[1])

    # Chinese remainder theorem
    a = bus_sorted[0][0]
    n = 1

    for i in range(len(bus_sorted) - 1):
        n *= bus_sorted[i][1]
        rem = bus_sorted[i+1][0]
        mod = bus_sorted[i+1][1]
        while True:
            if a % mod == rem:
                break
            a += n

    print(a)


if __name__ == '__main__':
    main()
