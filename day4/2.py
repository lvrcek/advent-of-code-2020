#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 4, Part 2
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


def is_invalid(key, value):
    if key == 'byr' and (int(value) < 1920 or int(value) > 2002):
        return True
    if key == 'iyr' and (int(value) < 2010 or int(value) > 2020):
        return True
    if key == 'eyr' and (int(value) < 2020 or int(value) > 2030):
        return True
    if key == 'hgt':
        if value[-2:] == 'cm':
            if int(value[:-2]) < 150 or int(value[:-2]) > 193:
                return True
        elif value[-2:] == 'in':
            if int(value[:-2]) < 59 or int(value[:-2]) > 76:
                return True
        else:
            return True
    if key == 'hcl':
        if value[0] != '#':
            return True
        value = value[1:]
        if len(value) != 6:
            return True
        for c in value:
            if not (c.isdigit() or c in 'abcdef'):
                return True
    if key == 'ecl':
        if value not in ('amb', 'blu', 'brn', 'grn', 'gry', 'hzl', 'oth'):
            return True
    if key == 'pid':
        if len(value) != 9:
            return True
    return False


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
                if key != 'cid' and value == -1 or is_invalid(key, value):
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
