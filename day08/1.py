#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 8, Part 1
"""


def solve(lines):
    i = 0
    acc = 0
    used = set()
    while True:
        if i in used:
            return acc
        else:
            used.add(i)
        op, arg = lines[i].split()
        if op == 'nop':
            i += 1
            continue
        if op == 'acc':
            acc += int(arg)
            i += 1
            continue
        if op == 'jmp':
            i += int(arg)
            continue


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    acc = solve(lines)

    print(acc)


if __name__ == '__main__':
    main()
