#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 16, Part 2
"""


import re
from collections import defaultdict


def parse(handle):
    rules = {}

    for line in handle:
        line = line.strip()
        if len(line) == 0:
            break
        r = r'([ a-z]*): (\d*)-(\d*) or (\d*)-(\d*)'
        rule, a1, b1, a2, b2 = re.findall(r, line)[0]
        a1, b1, a2, b2 = int(a1), int(b1), int(a2), int(b2)
        rules[rule] = (range(a1, b1 + 1), range(a2, b2 + 1))

    for line in handle:
        line = line.strip()
        if len(line) == 0:
            break
        if line == 'your ticket:':
            continue
        your_ticket = list(map(int, line.split(',')))

    nearby_tickets = []

    for line in handle:
        line = line.strip()
        if len(line) == 0:
            break
        if line == 'nearby tickets:':
            continue
        nearby_tickets.append(list(map(int, line.split(','))))

    return rules, your_ticket, nearby_tickets


def main():
    with open('in.txt') as f:
        rules, your_ticket, nearby_tickets = parse(f)

    nearby_valid = []
    counter = 0

    for nearby in nearby_tickets:
        valid = True
        for el in nearby:
            for rule, ranges in rules.items():
                if el in ranges[0] or el in ranges[1]:
                    break
            else:
                valid = False
                counter += el
        if valid:
            nearby_valid.append(nearby)

    decoded = defaultdict(set)
    changes = True

    while True:
        if not changes:
            break
        for rule, ranges in rules.items():
            changes = False
            for i, el_list in enumerate(zip(*nearby_valid)):
                found = True
                for el in el_list:
                    if el not in ranges[0] and el not in ranges[1]:
                        found = False
                        break
                if found:
                    if not i in decoded[rule]:
                        decoded[rule].add(i)
                        changes = True

    decoded = dict(sorted(decoded.items(), key=lambda item: len(item[1])))
    used = set()
    mul = 1

    for key, value in decoded.items():
        value = value - used
        v = value.pop()
        used.add(v)
        if 'departure' in key:
            mul *= your_ticket[v]

    print(mul)


if __name__ == '__main__':
    main()
