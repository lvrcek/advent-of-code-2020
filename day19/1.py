#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 19, Part 1
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
            r1 = tuple(map(int, rule1.strip().split()))
            r2 = tuple(map(int, rule2.strip().split()))
            d[rule_num] = [r1, r2]
        else:
            rules = [tuple(map(int, rest.strip().split()))]
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
    with open('in.txt') as f:
        rules = parse(f)

        start = time()
        get_all_strings(rules, 0)
        variations = set(memo[0])
        counter = 0
        for line in f:
            line = line.strip()
            counter += line in variations

    print(counter)

    end = time()
    print(f'{end - start} s')


if __name__ == '__main__':
    main()
