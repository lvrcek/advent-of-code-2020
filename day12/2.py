#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 12, Part 1
"""


class Ship:

    def __init__(self, x, y, w_x, w_y):
        self.x = x
        self.y = y
        self.w_x = w_x
        self.w_y = w_y

    def N(self, n):
        self.w_y += n

    def S(self, n):
        self.w_y -= n

    def E(self, n):
        self.w_x += n

    def W(self, n):
        self.w_x -= n

    def F(self, n):
        diff_x = self.w_x - self.x
        diff_y = self.w_y - self.y
        self.x += n * diff_x
        self.y += n * diff_y
        self.w_x += n * diff_x
        self.w_y += n * diff_y

    def R(self, deg):
        tmp_x = self.x
        tmp_y = self.y
        self.x = 0
        self.y = 0
        self.w_x -= tmp_x
        self.w_y -= tmp_y

        if deg == 90:
            self.w_x, self.w_y = self.w_y, -self.w_x
        elif deg == 180:
            self.w_x, self.w_y = -self.w_x, -self.w_y
        elif deg == 270:
            self.w_x, self.w_y = -self.w_y, self.w_x

        self.x += tmp_x
        self.y += tmp_y
        self.w_x += tmp_x
        self.w_y += tmp_y

    def L(self, deg):
        self.R(360 - deg)


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    ship = Ship(0, 0, 10, 1)
    for line in lines:
        action, n = line[0], int(line[1:])
        eval(f'ship.{action}({n})')

    pos = abs(ship.x) + abs(ship.y)
    print(pos)


if __name__ == '__main__':
    main()
