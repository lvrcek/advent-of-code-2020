#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 7, Part 1
"""


rule_dict = {}
correct = set()
incorrect = set()

counter = 0


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
            rule.append(color)
        rule_dict[new_color] = rule


def solve(color, query):
    global counter
    if color in correct:
        return True
    if color in incorrect:
        return False
    if query in rule_dict[color]:
        counter += 1
        correct.add(color)
        return True

    for new_color in rule_dict[color]:
        if solve(new_color, query):
            counter += 1
            correct.add(color)
            return True
    incorrect.add(color)
    return False


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    parse(lines)
    query = 'shiny gold'
    for c in rule_dict.keys():
        solve(c, query)

    print(counter)


if __name__ == '__main__':
    main()
