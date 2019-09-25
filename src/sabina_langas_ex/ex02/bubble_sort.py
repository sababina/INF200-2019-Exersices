# -*- coding: utf-8 -*-

__author__ = 'Sabina Langås'
__email__ = 'sabinal@nmbu.no'


def bubble_sort(data):
    new_sorted_list = list(data)

    for i in range(1, len(new_sorted_list)):
        for j in range(0, (len(new_sorted_list)-i)):
            if new_sorted_list[j] > new_sorted_list[j+1]:
                new_sorted_list[j], new_sorted_list[j + 1] = new_sorted_list[j+1], new_sorted_list[j]
    return new_sorted_list


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
