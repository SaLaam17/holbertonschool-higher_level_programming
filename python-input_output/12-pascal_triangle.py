#!/usr/bin/python3
"""
Module
"""
def pascal_triangle(n):
    """
    Function that returns a list of lists of integers
    representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return [] 
    #list_1 = [1]
    #list_2 = [list_1[0], list_1[0]]
    #list_3 = [list_2[0], list_2[0] + list_2[1], list_2[0]]
    #list_4 = [list_3[0], list_3[0] + list_3[1], list_3[1] + list_3[2], list_3[0]]
    #list_5 = [list_4[0], list_4[0] + list_4[1], list_4[1] + list_4[2], list_4[2] + list_4[3], list_4[0]]


    #list_1 = [1]
    #list_2 = [list_1[0], list_1[0]]
    #list_3 = [list_1[0], 2 * list_1[0], list_1[0]]
    #list_4 = [list_1[0], 3 * list_1[0], 3 * list_1[0], list_1[0]]
    #list_5 = [list_1[0], 4 * list_1[0], 6 * list_1[0], 4 * list_1[0], list_1[0]]
    #triangle = [list_1, list_2]

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
