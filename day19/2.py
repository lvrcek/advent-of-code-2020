#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 19, Part 2
"""

from time import time


memo = {}


def parse(f):
    d = {}
    for line in f:
        line = line.strip()
        if len(line) == 0:
            return d
        rule_num, rest = line.split(':')
        rule_num = int(rule_num)
        rest = rest.strip()
        if '"' in rest:
            c = rest[1]
            d[rule_num] = c
        elif '|' in rest:
            rule1, rule2 = rest.split('|')
            # print(rest)
            r1 = tuple(map(int, rule1.strip().split()))
            r2 = tuple(map(int, rule2.strip().split()))
            d[rule_num] = [r1, r2]
        else:
            rules = []
            rules.append(tuple(map(int, rest.strip().split())))
            d[rule_num] = rules
    return d


def get_all_strings(rules_dict, rule):
    if rule in memo:
        return memo[rule]

    if isinstance(rules_dict[rule], str):
        memo[rule] = list(rules_dict[rule])
        return memo[rule]

    groups = rules_dict[rule]
    new_strings = []

    for group in groups:
        append_prefix = ['']

        for next_rule in group:
            strings = get_all_strings(rules_dict, next_rule)
            new = [a + s for a in append_prefix for s in strings]
            append_prefix = new.copy()

        new_strings.extend(append_prefix)

    memo[rule] = new_strings
    return new_strings


def main():
    with open('in2.txt') as f:
        rules = parse(f)

        start = time()
        get_all_strings(rules, 42)
        get_all_strings(rules, 31)
        rules_42 = memo[42]
        rules_31 = memo[31]

        inc = len(rules_31[0])

        counter = 0
        for line in f:
            line = line.strip()
            # counter += is_valid(line)
            loc = len(line)
            correct = True
            count = 0
            while True:
                if loc == 0:
                    correct = False
                    break
                if line[loc-inc:loc] in rules_31:
                    loc -= inc
                    count += 1
                else:
                    break
            if not correct or count == 0:
                continue

            while True:
                if loc == 0:
                    correct = False
                    break
                if count == 0:
                    break
                if line[loc-inc:loc] in rules_42:
                    loc -= inc
                    count -= 1
                else:
                    correct = False
                    break
            if not correct:
                continue

            while True:
                if loc == 0:
                    correct = True
                    break
                if line[loc-inc:loc] in rules_42:
                    loc -= inc
                else:
                    correct = False
                    break

            if correct:
                counter += 1
                continue

    print(counter)

    end = time()
    print(f'{end - start} s')


if __name__ == '__main__':
    main()
