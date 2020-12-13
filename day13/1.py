#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 13, Part 1
"""


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    arrival = int(lines[0].strip())
    bus_ids = []

    for n in lines[1].strip().split(','):
        if n == 'x':
            continue
        else:
            bus_ids.append(int(n))

    waiting_time = [(n - arrival % n, n) for n in bus_ids]
    min_time = waiting_time[0][0]
    first_bus = waiting_time[0][1]

    for minutes, bus in waiting_time[1:]:
        if minutes < min_time:
            min_time = minutes
            first_bus = bus

    print(min_time * first_bus)


if __name__ == '__main__':
    main()
