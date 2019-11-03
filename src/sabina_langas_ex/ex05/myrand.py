# -*- coding: utf-8 -*-

__author__ = 'Sabina Langås'
__email__ = 'sabinal@nmbu.no'


class LCGRand:
    a = 7 ** 5
    m = 2 ** 31 - 1

    def __init__(self, seed):
        """
        Initialise a linear congruence random number generator

        Arguments
        ---------
        seed : int
            The initial seed for the generator
        """

        self.previous = seed

    def rand(self):
        """
        Generate a single random number.

        Returns
        -------
        int
            A random integer
        """

        self.previous = LCGRand.a * self.previous % LCGRand.m

        return self.previous

    def random_sequence(self, length):
        """
        Generates a random_sequence, with given length

        Arguments
        ---------
        length : int
            The wished length of random_sequence

        Returns
        -------
        int
            A random sequence
        """

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