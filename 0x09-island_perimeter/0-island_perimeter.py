#!/usr/bin/python3
"""0-island_perimeter module
"""


def island_perimeter(grid):
    """island_perimeter function that returns the perimeter of the island

    Args:
        grid (list[int]): grid representation of the island

    Returns:
        int: perimeter of the island
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                if i == 0 or not grid[i - 1][j]:
                    perimeter += 1
                if j == 0 or not grid[i][j - 1]:
                    perimeter += 1
                if i == len(grid) - 1 or not grid[i + 1][j]:
                    perimeter += 1
                if j == len(grid[i]) - 1 or not grid[i][j + 1]:
                    perimeter += 1
    return perimeter
