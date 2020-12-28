#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 23, Part 2
"""


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next =Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return ' -> '.join(nodes)

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception('List is empty')

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception(f'Node with data {target_node_data} not found')

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f'Node with data {target_node_data} node found')

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f'Node with data {target_node_data} not found')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


def play_game(cups, start):
    picked_cups = cups[start], cups[cups[start]], cups[cups[cups[start]]]

    destination = start - 1

    while True:
        if destination in picked_cups:
            destination -= 1
        else:
            if destination == 0:
                destination = 1000000
            else:
                break

    new_start = cups[picked_cups[2]]
    dest_next = cups[destination]
    cups[destination] = picked_cups[0]
    cups[picked_cups[2]] = dest_next
    cups[start] = new_start
    start = new_start
    return cups, start


def main():
    with open('in.txt') as f:
        lines = f.read()

    cups = list(map(int, list(lines.strip())))
    cups += range(10, 1000000+1)
    cups_dict = {}
    for i in range(len(cups) - 1):
        cups_dict[cups[i]] = cups[i+1]
    cups_dict[cups[-1]] = cups[0]

    start = cups[0]
    for i in range(10000000):
        print(f'move {i+1}')
        cups_dict, start = play_game(cups_dict, start)

    cup1 = cups_dict[1]
    cup2 = cups_dict[cup1]
    print(cup1, cup2)
    print(cup1 * cup2)


if __name__ == '__main__':
    main()
