#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 25, Part 1
"""


def main():
    with open('in.txt') as f:
        card_key, door_key = map(int, f.readlines())

    subject_number = 7

    value = 1
    card_loop = 0
    while True:
        card_loop += 1
        value *= subject_number
        value %= 20201227
        if value == card_key:
            print(card_loop)
            break

    value = 1
    door_loop = 0
    while True:
        door_loop += 1
        value *= subject_number
        value %= 20201227
        if value == door_key:
            print(door_loop)
            break

    encryption_key = 1
    subject_number = card_key
    for _ in range(door_loop):
        encryption_key *= subject_number
        encryption_key %= 20201227

    print(encryption_key)


if __name__ == '__main__':
    main()
