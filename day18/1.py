#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 18, Part 1
"""


def calculate(expression):
    a = expression[0]
    for k in range(1, len(expression), 2):
        op = expression[k]
        b = expression[k + 1]
        if op == '+':
            a += b
        else:
            a *= b
    return a


def evaluate(line):
    stack = []
    i = 0

    while True:
        if i == len(line):
            res = calculate(stack)
            return res

        elif line[i] in '+*(':
            stack.append(line[i])
            i += 1

        elif line[i].isdigit():
            j = i
            num = ''
            while j < len(line) and line[j].isdigit():
                num += line[j]
                j += 1
            stack.append(int(num))
            i = j

        elif line[i] == ')':
            expression = []
            while True:
                n = stack.pop()
                if n == '(':
                    break
                expression.append(n)
            expression = list(reversed(expression))
            res = calculate(expression)
            stack.append(res)
            i += 1


def main():
    with open('in.txt') as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        line = line.strip().replace(' ', '')
        total += evaluate(line)

    print(total)


if __name__ == '__main__':
    main()
