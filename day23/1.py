#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 23, Part 1
"""


def play_game(cups):
    max_cup, min_cup = max(cups), min(cups)
    picked_cups = cups[1:4]
    # print(picked_cups)
    cups = [cups[0]] + cups[4:]
    destination = cups[0] - 1

    while True:
        if destination in picked_cups:
            destination -= 1
        else:
            if destination < min_cup:
                destination = max_cup
            else:
                break
    # print(destination)
    dest_idx = cups.index(destination)
    cups_1, cups_2 = cups[:dest_idx+1], cups[dest_idx+1:]
    cups = cups_1 + picked_cups + cups_2
    cups = cups[1:] + [cups[0]]
    return cups


def main():
    with open('in.txt') as f:
        lines = f.read()

    cups = list(map(int, list(lines.strip())))
    # cups += range(10, 1000000+1)
    # print(len(cups))
    # exit()
    for i in range(100):
        print(f'move {i+1}')
        # print(cups)
        cups = play_game(cups.copy())

    idx = cups.index(1)
    # cups = cups[idx+1:idx+3]
    cups_1, cups_2 = cups[:idx], cups[idx+1:]
    cups = cups_2 + cups_1
    print(''.join(map(str, cups)))


if __name__ == '__main__':
    main()
