# -*- coding: utf-8 -*-

__author__ = 'Sabina Langås'
__email__ = 'sabinal@nmbu.no'


def bubble_sort(data):
    sorted_list = list(data)

    for i in range(1, len(sorted_list)):
        for j in range(0, (len(sorted_list)-i)):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j+1], sorted_list[j]
    return sorted_list


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
