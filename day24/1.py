#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 24, Part 1
"""


def print_floor(floor):
    floor = [' '.join(map(str, f)) for f in floor]
    floor = '\n'.join(floor)
    print(floor)


def parse(line):
    movement = []
    i = 0
    while i < len(line):
        if line[i] in 'ns':
            command = line[i] + line[i+1]
            movement.append(command)
            i += 2
            continue
        else:
            command = line[i]
            movement.append(command)
            i += 1
            continue
    return movement


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    floor = [[0 for _ in range(2000)] for _ in range(600)]

    for line in lines:
        line = line.strip()
        movement = parse(line)

        x = 300
        y = 1000
        for move in movement:
            if move == 'e':
                y += 2
            if move == 'w':
                y -= 2
            if move == 'sw':
                x += 1
                y -= 1
            if move == 'nw':
                x -= 1
                y -= 1
            if move == 'se':
                x += 1
                y += 1
            if move == 'ne':
                x -= 1
                y += 1

        floor[x][y] = 1 - floor[x][y]

    counter = 0
    for row in floor:
        for tile in row:
            counter += tile
    print(counter)


if __name__ == '__main__':
    main()
