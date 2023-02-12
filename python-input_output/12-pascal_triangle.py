#!/usr/bin/python3
""" defines the pascal_triangle function """


def pascal_triangle(n):
    """ returns the pascal triangle of n """
    pascal_triangle_strategy = [[1]]
    list = [1, 1]

    if n <= 0:
        return []
    for i in range(1, n):
        prev_list = list
        list = [1]
        for j in range(0, i-1):
            list.append(prev_list[j] + prev_list[j + 1])
        list.append(1)
        pascal_triangle_strategy.append(list)
    return pascal_triangle_strategy
