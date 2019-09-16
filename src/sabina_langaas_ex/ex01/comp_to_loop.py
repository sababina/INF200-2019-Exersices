# -*- coding: utf-8 -*-

"""
Solution to task B on exercise 01 in INF200
"""


def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    squares = []
    for k in range(n):
        if k % 3 == 1:
            squares.append(k**2)
    return squares


if __name__ == '__main__':

    number = int(input('Enter a number'))

    if squares_by_comp(number) != squares_by_loop(number):
        print('ERROR!')
    else:
        print('Success')
