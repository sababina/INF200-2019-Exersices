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
        Generates a random sequence, with given length of many numbers it
        should be

        Arguments
        ---------
        length : int
            The number of random numbers that should be generated in the
            sequence

        Returns
        -------
        int
            A random sequence of numbers
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


class RandIter:

    def __init__(self, random_number_generator, length):
        """
        Arguments
        ---------
        random_number_generator :
            A random number generator with a ``rand`` method that
            takes no arguments and returns a random number.

        length : int
            The number of random numbers to generate
        """
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        """
        Initialise the iterator.

        Returns
        -------
        self : RandIter

        Raises
        ------
        RuntimeError
            If iter is called twice on the same RandIter object.
        """
        if self.num_generated_numbers is not None:
            raise RuntimeError()

        self.num_generated_numbers = 0

        return self

    def __next__(self):
        """
        Generate the next random number.

        Returns
        -------
        int
            A random number.

        Raises
        ------
        RuntimeError
            If the ``__next__`` method is called before ``__iter__``.
        StopIteration
            If ``self.length`` random numbers are generated.
        """

        if self.num_generated_numbers is None:
            raise RuntimeError('Next random number can´t be generated before '
                               'calling ''before initialise the iterator '
                               )

        if self.num_generated_numbers == self.length:
            raise StopIteration('All numbers is generated')

        number = self.generator.rand()

        self.num_generated_numbers += 1

        return number

