#!/usr/bin/python3
"""Pascal's Triangle"""

def pascal_triangle(n):
    """
    A function that returns a list
    of lists of integers representing the
    Pascal's triangle of n:
    - Returns an empty list if n <= 0
    - Assumes n will be always an integer
    """
    pascal_tri = []

    if n <= 0:
        return pascal_tri

    for i in range(n):
        if i == 0:
            pascal_tri.append([1])
        else:
            cur_row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    cur_row.append(1)
                else:
                    cur_row.append(pascal_tri[i - 1][j - 1] + pascal_tri[i - 1][j])
            pascal_tri.append(cur_row)

    return pascal_tri
