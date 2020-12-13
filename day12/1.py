#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 12, Part 1
"""

from enum import IntEnum


class Direction(IntEnum):
    N = 0
    E = 1
    S = 2
    W = 3


class Ship:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def N(self, n):
        self.y += n

    def S(self, n):
        self.y -= n

    def E(self, n):
        self.x += n

    def W(self, n):
        self.x -= n

    def F(self, n):
        self.y += n * (self.direction == Direction.N)
        self.x += n * (self.direction == Direction.E)
        self.y -= n * (self.direction == Direction.S)
        self.x -= n * (self.direction == Direction.W)

    def R(self, deg):
        self.direction += int(deg / 90)
        self.direction %= 4

    def L(self, deg):
        self.R(360 - deg)


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    ship = Ship(0, 0, Direction.E)
    for line in lines:
        line = line.strip()
        action, n = line[0], int(line[1:])
        eval(f'ship.{action}({n})')

    pos = abs(ship.x) + abs(ship.y)
    print(pos)


if __name__ == '__main__':
    main()
