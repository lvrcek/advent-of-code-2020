#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 7, Part 2
"""


color_dict = {}
rule_dict = {}


def parse(lines):
    for line in lines:
        line = line.strip().split()

        new_color = ' '.join(line[0:2])
        rule = []
        while True:
            line = line[4:]
            if len(line) == 0 or line[0] == 'no':
                break
            num = int(line[0])
            color = ' '.join(line[1:3])
            rule.append((color, num))
        rule_dict[new_color] = rule


def solve(color):
    add = 0
    if len(rule_dict[color]) == 0:
        return 0
    for bag, num in rule_dict[color]:
        add += num
        if len(rule_dict[bag]) == 0:
            continue
        mul = num * solve(bag)
        add += mul
    return add


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    parse(lines)
    query = 'shiny gold'
    add = solve(query)

    print(add)


if __name__ == '__main__':
    main()
