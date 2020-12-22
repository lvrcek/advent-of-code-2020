#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 20, Part 2
"""

from math import sqrt


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


def rotate(tile):
    tile_new = []
    size = len(tile.split()[0].strip())
    for i in range(size-1, -1, -1):
        new_row = ''
        for row in tile.split():
            new_row += row[i]
        tile_new.append(new_row)
    tile_new = '\n'.join(tile_new)
    return tile_new


def flip_horizontal(tile):
    tile_new = []
    for row in tile.split('\n'):
        row = row.strip()
        row = ''.join(list(reversed(row)))
        tile_new.append(row)
    tile_new = '\n'.join(tile_new)
    return tile_new


def flip_vertical(tile):
    tile_new = []
    for row in reversed(tile.split()):
        row = row.strip()
        tile_new.append(row)
    tile_new = '\n'.join(tile_new)
    return tile_new


def print_id_grid(grid):
    grid = [[str(id).ljust(5, ' ') for id in g] for g in grid]
    grid = [' '.join(g) for g in grid]
    grid = '\n'.join(grid)
    print(grid)


def print_tile_grid(grid):
    grid = [' '.join(g.replace('\n', '')) for g in grid]
    grid = '\n\n'.join(grid)
    print(grid)


def concatenate(grid):
    new_grid = []
    size = len(grid[0][0])
    for row in grid:
        cat_tile = ''
        for i in range(size):
            r = ''
            for tile in row:
                r += tile[i]
                r += ' '
            r = r[:-1] + '\n'
            cat_tile += r
        new_grid.append(cat_tile)
    new_grid = '\n'.join(new_grid)
    return new_grid


def concatenate_and_remove(grid):
    new_grid = []
    size = len(grid[0][0])
    for row in grid:
        cat_tile = ''
        for i in range(1, size-1):
            r = ''
            for tile in row:
                r += tile[i][1:-1]
            r = r + '\n'
            cat_tile += r
        new_grid.append(cat_tile)
    new_grid = ''.join(new_grid)
    return new_grid


def get_positions(grid, i, j):
    positions = [
        grid[i][j + 18],
        grid[i + 1][j], grid[i + 1][j + 5], grid[i + 1][j + 6], grid[i + 1][j + 11], grid[i + 1][j + 12],
        grid[i + 1][j + 17], grid[i + 1][j + 18], grid[i + 1][j + 19], grid[i + 2][j + 1],
        grid[i + 2][j + 4], grid[i + 2][j + 7], grid[i + 2][j + 10], grid[i + 2][j + 13], grid[i + 2][j + 16]
    ]
    return positions


def main():
    with open('in.txt') as f:
        lines = f.read()

    tiles = {}
    for entry in lines.split('\n\n'):
        entry = entry.split('\n')
        id = int(entry[0][-5:-1])
        tile = '\n'.join(entry[1:])
        tiles[id] = tile

    size = int(sqrt(len(tiles)))

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

    used = set()
    id_grid = [[-1 for _ in range(size)] for _ in range(size)]
    tile_grid = [[[] for _ in range(size)] for _ in range(size)]

    x = 0
    y = 0

    for id, tile in tiles.items():
        edges = find_edges(tile)
        up, down, left, right = edges
        if up in edge_dict and left in edge_dict and edge_dict[up] == edge_dict[left] == 1:
            id_grid[x][y] = id
            tile_grid[x][y] = tile.split()
            matching_right = right
            matching_down = down
            used.add(id)
            y += 1
            break

    counter = 1

    while True:
        if counter == size * size:
            break
        for id, tile in tiles.items():
            if id in used:
                continue

            current_tile = tile
            tries = 0
            while True:
                if tries > 8:  # Number of tile orientations
                    break
                up, down, left, right = find_edges(current_tile)
                tries += 1
                if y > 0:
                    if matching_right == left:
                        used.add(id)
                        id_grid[x][y] = id
                        tile_grid[x][y] = current_tile.split()
                        if y == size - 1:
                            x += 1
                            y = 0
                        else:
                            y += 1
                            matching_right = right
                        counter += 1
                        break
                    else:
                        if tries == 4:
                            current_tile = flip_vertical(current_tile)
                        else:
                            current_tile = rotate(current_tile)

                if y == 0:
                    if matching_down == up:
                        used.add(id)
                        id_grid[x][y] = id
                        tile_grid[x][y] = current_tile.split()
                        if y == size - 1:
                            x += 1
                            y = 0
                        else:
                            y += 1
                            matching_right = right
                            matching_down = down
                        counter += 1
                        break
                    else:
                        if tries == 4:
                            current_tile = flip_vertical(current_tile)
                        else:
                            current_tile = rotate(current_tile)

    # print_id_grid(id_grid)

    sea_grid = concatenate_and_remove(tile_grid)
    monster_counter = 0
    tries = -1

    while monster_counter == 0:
        tries += 1
        if tries == 4:
            sea_grid = flip_vertical(sea_grid)
        sea_grid = rotate(sea_grid)
        sea_list = [line.strip() for line in sea_grid.split()]

        for i in range(len(sea_list)-2):
            for j in range(0, len(sea_list[0]) - 19):
                positions = get_positions(sea_list, i, j)
                if all([p == '#' for p in positions]):
                    monster_counter += 1

    # print(monster_counter)
    print(sea_grid.count('#') - len(positions) * monster_counter)


if __name__ == '__main__':
    main()
