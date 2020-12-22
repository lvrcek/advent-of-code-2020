#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 20, Part 2
"""


def find_edges(tile):
    tile = tile.split('\n')
    up = tile[0]
    down = tile[-1]
    left = ''
    right = ''
    for row in tile:
        left += row[0]
        right += row[-1]
    return up, down, left, right


def print_map(map):
    map = [''.join(str(l)) for l in map]
    print(map)


def main():
    with open('in.txt') as f:
        lines = f.read()

    tiles = {}
    for entry in lines.split('\n\n'):
        entry = entry.split('\n')
        id = int(entry[0][-5:-1])
        tile = '\n'.join(entry[1:])
        tiles[id] = tile

    map = [[-1 for _ in range(12)] for _ in range(12)]

    occurance = {}
    edge_dict = {}
    for id, tile in tiles.items():
        edges = find_edges(tile)
        for edge in edges:
            reverse = ''.join(list(reversed(edge)))
            if edge not in edge_dict.keys() and reverse not in edge_dict.keys():
                edge_dict[edge] = 1
            else:
                if edge in edge_dict.keys():
                    edge_dict[edge] += 1
                else:
                    edge_dict[reverse] += 1

    print(tiles)
    print(edge_dict)

    mul = 1
    counter = 0
    for id, tile in tiles.items():
        edges = find_edges(tile)
        count = 0
        for edge in edges:
            reverse = ''.join(list(reversed(edge)))
            if edge in edge_dict.keys():
                if edge_dict[edge] == 1:
                    count += 1
            elif reverse in edge_dict.keys():
                if edge_dict[reverse] == 1:
                    count += 1
        if count == 2:
            print(id)
            if counter == 0:
                map[0][0] = id
            elif counter == 1:
                map[0][11] = id
            elif counter == 2:
                map[11][0] = id
            else:
                map[11][11] = id
            mul *= id

    print_map(map)
    print(mul)
    # print(edge_dict)

    # Work in progress
    print('NOT SOLVED YET!!!')


if __name__ == '__main__':
    main()
