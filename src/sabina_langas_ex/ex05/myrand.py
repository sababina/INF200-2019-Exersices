# -*- coding: utf-8 -*-

__author__ = 'Sabina Langås'
__email__ = 'sabinal@nmbu.no'


class LCGRand:
    a = 7 ** 5
    m = 2 ** 31 - 1

    def __init__(self, seed):
        self.previous = seed

    def rand(self):
        self.previous = LCGRand.a * self.previous % LCGRand.m

        return self.previous

    def random_sequence(self, length):

        return RandIter(self, length)

    def infinite_random_sequence(self):
        """
        Generate an infinite sequence of random numbers.

        Yields
        ------
        int
            A random number.
        """
        while True:
            yield self.rand()