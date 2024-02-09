#!/usr/bin/python3
"""Module contains island_perimeter function"""


def island_perimeter(grid):
    """
    Functions returns the perimeter of the island described in grid
    grid: list of integers
        * 0 represents water
        * 1 represents land
        * each cell is a square, with a side length of 1
        * cells are connected horizontally/vertically (not diagonally)
        * grind is rectangular, with its width and height not exceeding 100
    The grid is surrounded by water
    """
    perimeter = 0

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 0:
                continue
            if grid[x][y] == 1:
                cellperimeter = 4
                if x - 1 > -1 and grid[x - 1][y] == 1:
                    cellperimeter = cellperimeter - 1
                if x + 1 < len(grid) and grid[x + 1][y] == 1:
                    cellperimeter = cellperimeter - 1
                if y - 1 > -1 and grid[x][y - 1] == 1:
                    cellperimeter = cellperimeter - 1
                if y + 1 < len(grid[x]) and grid[x][y + 1] == 1:
                    cellperimeter = cellperimeter - 1
                perimeter = perimeter + cellperimeter
    return perimeter
