#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 18, Part 2
"""


def calculate(expression):
    stack = []
    i = 0

    while True:
        if i == len(expression):
            break
        n = expression[i]
        if str(n) not in '+*':
            stack.append(n)
        elif n == '+':
            i += 1
            b = expression[i]
            a = stack.pop()
            stack.append(a + b)
        i += 1

    mul = 1
    for s in stack:
        mul *= s
    return mul


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
