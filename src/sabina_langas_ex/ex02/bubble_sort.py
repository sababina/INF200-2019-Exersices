# -*- coding: utf-8 -*-

__author__ = 'Sabina Langås'
__email__ = 'sabinal@nmbu.no'


def bubble_sort(data):
    """
    Sorts the data after teh bubble_sort algorithm

    :param data: The data that going to be sort

    :return: Returns the input sorted in a new list
    """
    sort_data = list(data)

    for i in range(1, len(sort_data)):
        for j in range(0, (len(sort_data) - i)):
            if sort_data[j] > sort_data[j + 1]:
                sort_data[j], sort_data[j + 1] = sort_data[j + 1], sort_data[j]
    return sort_data


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
