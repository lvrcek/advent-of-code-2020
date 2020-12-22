#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 22, Part 2
"""


def play_game(player1, player2):
    seen = {1: [], 2: []}
    while True:
        if len(player1) == 0:
            winner = 2
            break
        if len(player2) == 0:
            winner = 1
            break

        if player1 in seen[1] or player2 in seen[2]:
            winner = 1
            break

        else:
            seen[1].append(player1)
            seen[2].append(player2)

            p1 = player1[0]
            player1 = player1[1:]

            p2 = player2[0]
            player2 = player2[1:]

            if len(player1) >= p1 and len(player2) >= p2:
                winner, _, _ = play_game(player1[:p1].copy(), player2[:p2].copy())
            else:
                if p1 > p2:
                    winner = 1
                else:
                    winner = 2

            if winner == 1:
                player1.append(p1)
                player1.append(p2)
            else:
                player2.append(p2)
                player2.append(p1)

    return winner, player1, player2


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
            if p == 1:
                n = int(line)
                player1.append(n)
            else:
                n = int(line)
                player2.append(n)

    _, player1, player2 = play_game(player1, player2)

    player = player1 if len(player1) != 0 else player2

    score = 0
    for i, n in enumerate(reversed(player)):
        score += (i+1) * n

    print(score)


if __name__ == '__main__':
    main()
