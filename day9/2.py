#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 9, Part 2
"""


def find_sums(numbers):
    return [n + m for n in numbers for m in numbers]


def find_contig(numbers, wrong):
    for i in range(len(numbers)):
        contig = [numbers[i]]
        contig_sum = numbers[i]
        for j in range(i+1, len(numbers)):
            contig.append(numbers[j])
            contig_sum += numbers[j]
            if contig_sum > wrong:
                break
            if contig_sum == wrong:
                return min(contig) + max(contig)


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    numbers = list(map(int, lines))
    for i, number in enumerate(numbers):
        if i < 25:
            continue
        sums = find_sums(numbers[i-25:i])
        if number not in sums:
            minmax = find_contig(numbers[:i], number)
            print(minmax)
            break


if __name__ == '__main__':
    main()
