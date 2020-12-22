#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 22, Part 1
"""


def play_game(player1, player2):
    while True:
        if len(player1) == 0 or len(player2) == 0:
            break

        p1 = player1[0]
        player1 = player1[1:]

        p2 = player2[0]
        player2 = player2[1:]

        if p1 > p2:
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)

    return player1, player2


def main():
    with open('in.txt') as f:

        player1 = []
        player2 = []

        p = 1

        for line in f:
            line = line.strip()
            if 'Player' in line:
                continue
            if len(line) == 0:
                p = 2
                continue
            n = int(line)
            if p == 1:
                player1.append(n)
            else:
                player2.append(n)

    player1, player2 = play_game(player1, player2)

    player = player1 if len(player1) != 0 else player2

    score = 0
    for i, n in enumerate(reversed(player)):
        score += (i+1) * n

    print(score)


if __name__ == '__main__':
    main()
