# -*- coding: utf-8 -*-

__author__ = 'Sabina Langås'
__email__ = 'sabinal@nmbu.no'


class ListRand:

    def __init__(self, list_numbers):
        self.random_number = list_numbers.copy()
        self.next = 0

    def rand(self):
        if self.next >= len(self.random_number):
            raise RuntimeError("The last number has been delivered")

        number = self.random_number[self.next]
        self.next += 1

        return number


class LCGRand:
    a = 7 ** 5
    m = 2 ** 31 - 1

    def __init__(self, seed):
        self.previous = seed

    def rand(self):
        self.previous = LCGRand.a * self.previous % LCGRand.m

        return self.previous


if __name__ == '__main__':

    list_of_numbers_test = ListRand([5, 3, 4, 6, 8, 9])
    lcg_test = LCGRand(5)

    for i in range(6):
        print('Random number from LCGRand {} and from ListRand {}'.format(
         lcg_test.rand(), list_of_numbers_test.rand()))
