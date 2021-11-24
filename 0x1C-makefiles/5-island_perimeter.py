#!/usr/bin/python3
"""
This module contains a function called island_perimeter
"""


def island_perimeter(grid):
    """
    Returns the perimeter of an Island
    Args:
        grid(list): A list of list of integers
    """

    width = 0
    height = 0

    for nested_list in grid:
        counter = nested_list.count(1)
        if counter == 1:
            height += 1
            width = 1
        elif counter > 1:
            height += 1
            width = counter
    perimeter = 2 * (height + width)
    return perimeter
