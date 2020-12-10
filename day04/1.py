#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 4, Part 1
"""


class Passport:
    def __init__(self, byr=-1, iyr=-1, eyr=-1, hgt=-1, hfc=-1, ecl=-1, pid=-1, cid=-1):
        self.fields = {
            'byr': byr,
            'iyr': iyr,
            'eyr': eyr,
            'hgt': hgt,
            'hcl': hfc,
            'ecl': ecl,
            'pid': pid,
            'cid': cid,
        }


def parse(line):
    fields = line.split()
    field_dict = {}
    for field in fields:
        key1, value1 = field.split(':')
        field_dict[key1] = value1
    return field_dict


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    counter = 0
    total_passports = 0
    passport = Passport()

    for line in lines:
        line = line.strip()
        if len(line) == 0:
            for key, value in passport.fields.items():
                if key != 'cid' and value == -1:
                    counter += 1
                    break
            total_passports += 1
            passport = Passport()
        d = parse(line)
        for key, value in d.items():
            passport.fields[key] = value

    print(total_passports - counter)


if __name__ == '__main__':
    main()
