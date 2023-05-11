#!/usr/bin/python3
"""rotate_2d_matrix module
"""


def rotate_2d_matrix(matrix):
    """rotate_2d_matrix function

    Args:
        matrix (list): 2D matrix to rotate
    """
    matrix[:] = zip(*matrix[::-1])
