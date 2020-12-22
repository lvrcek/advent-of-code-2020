#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2020
Day 21, Part 1
"""

import re
from copy import deepcopy


def remove_from_lists(ingredients_list, allergens_list, ing, alg):
    for ingredients, allergens in zip(ingredients_list, allergens_list):
        if ing in ingredients:
            ingredients.remove(ing)
        if alg in allergens:
            allergens.remove(alg)

def main():
    with open('in.txt') as f:
        lines = f.readlines()

    ingredients_list = []
    allergens_list = []

    all_ingredients = set()
    all_allergens = set()

    ingredients_dict = {}
    for line in lines:
        line = line.strip()
        regex = r'([a-z, ]*) \(contains ([a-z, ]*)\)'
        ingredients, allergens = re.findall(regex, line)[0]
        ingredients = ingredients.split()
        allergens = allergens.replace(',', '').split()
        ingredients_list.append(ingredients)
        allergens_list.append(allergens)

        all_ingredients |= set(ingredients)
        all_allergens |= set(allergens)

    ingredients_original = deepcopy(ingredients_list)

    ingredients_dict = {}

    while True:
        change = False

        i = -1
        while True:
            i += 1
            if i >= len(ingredients_list):
                break
            ing_intersect = set(ingredients_list[i])
            alg_intersect = set(allergens_list[i])
            j = -1
            while True:
                j += 1
                if j == i:
                    continue
                if j >= len(ingredients_list):
                    break
                if len(ing_intersect & set(ingredients_list[j])) > 0 and len(alg_intersect & set(allergens_list[j]))>0:
                    ing_intersect = ing_intersect & set(ingredients_list[j])
                    alg_intersect = alg_intersect & set(allergens_list[j])
                else:
                    continue
                if len(ing_intersect) == len(alg_intersect) == 1:

                    ing = ing_intersect.pop()
                    alg = alg_intersect.pop()
                    ingredients_dict[ing] = alg
                    remove_from_lists(ingredients_list, allergens_list, ing, alg)
                    ing_intersect = set(ingredients_list[i])
                    alg_intersect = set(allergens_list[i])
                    change = True

        for ingredients, allergens in zip(ingredients_list, allergens_list):
            ingredients = set(ingredients)
            allergens = set(allergens)
            if len(ingredients) == len(allergens):
                while len(ingredients) > 0:
                    ing = ingredients.pop()
                    alg = allergens.pop()
                    ingredients_dict[ing] = alg
                    remove_from_lists(ingredients_list, allergens_list, ing, alg)
                    change = True

        if not change:
            break

    safe_ingredients = all_ingredients - set(ingredients_dict.keys())
    counter = 0
    for ingredients in ingredients_original:
        for ingredient in ingredients:
            counter += ingredient in safe_ingredients

    print(counter)


if __name__ == '__main__':
    main()
