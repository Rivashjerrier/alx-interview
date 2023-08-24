#!/usr/bin/python3
"""
0-rotate_2d_matrix.py module
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise
    """
    size = len(matrix)
    rotate = []

    for i in range(size):
        rows = []
        for row in reversed(matrix):
            rows.append(row[i])
        rotate.append(rows)
    for i in range(size):
        matrix[i] = rotate[i]
