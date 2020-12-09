#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 8, Part 2
"""


def solve(lines):
    i = 0
    acc = 0
    used = set()
    while True:
        if i == len(lines):
            return True, acc
        if i in used:
            return False, acc
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

    for i in range(len(lines)):
        line = lines[i]
        if line[:3] == 'nop':
            tmp = 'jmp' + line[3:]
        elif line[:3] == 'jmp':
            tmp = 'nop' + line[3:]
        else:
            continue
        lines[i] = tmp
        is_done, acc = solve(lines)
        lines[i] = line
        if is_done:
            break

    print(acc)


if __name__ == '__main__':
    main()
