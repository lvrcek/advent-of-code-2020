#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 8, Part 2
"""


def run(lines):
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

    lines_2 = lines.copy()
    lines = [line.strip() for line in lines]
    lines_2 = [line.strip() for line in lines_2]

    for i in range(len(lines)):
        op, arg = lines[i].split()
        if op == 'nop':
            new_line = 'jmp ' + arg
        elif op == 'jmp':
            new_line = 'nop ' + arg
        else:
            continue
        lines_2[i] = new_line
        is_done, acc = run(lines_2)
        lines_2 = lines.copy()
        if is_done:
            break

    print(acc)


if __name__ == '__main__':
    main()
