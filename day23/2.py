#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 23, Part 2
"""


def play_game(cups, start):
    picked_cups = cups[start], cups[cups[start]], cups[cups[cups[start]]]

    destination = start - 1

    while True:
        if destination in picked_cups:
            destination -= 1
        else:
            if destination == 0:
                destination = 1000000
            else:
                break

    new_start = cups[picked_cups[2]]
    dest_next = cups[destination]
    cups[destination] = picked_cups[0]
    cups[picked_cups[2]] = dest_next
    cups[start] = new_start
    start = new_start
    return cups, start


def main():
    with open('in.txt') as f:
        lines = f.read()

    cups = list(map(int, list(lines.strip())))
    cups += range(10, 1000000+1)
    cups_dict = {}
    for i in range(len(cups) - 1):
        cups_dict[cups[i]] = cups[i+1]
    cups_dict[cups[-1]] = cups[0]

    start = cups[0]
    for i in range(10000000):
        print(f'move {i+1}')
        cups_dict, start = play_game(cups_dict, start)

    cup1 = cups_dict[1]
    cup2 = cups_dict[cup1]
    print(cup1, cup2)
    print(cup1 * cup2)


if __name__ == '__main__':
    main()
