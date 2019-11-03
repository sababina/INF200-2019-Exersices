# -*- coding: utf-8 -*-

__author__ = 'Sabina Langås'
__email__ = 'sabinal@nmbu.no'

import random


class Walker:
    """
    Simulates a random walker.
    A walker starts at a given position and has a home.
    """

    def __init__(self, start_position, home_position):
        """
        :param start_position: The value at where the walker starts
        :param home_position: The value of where the walker's home is
        """
        self.x = start_position
        self.h = home_position
        self.steps = 0

    def move(self):
        """
        Moves the walker  by +1 or -1 step, with equal probability.
        """
        self.x += 2 * random.randint(0, 1) - 1
        self.steps += 1

    def is_at_home(self):
        """
        Returns True, if the walker have reach home safely
        """
        return self.x == self.h

    def get_position(self):
        """
        Returns the walker's current position
        """
        return self.x

    def get_steps(self):
        """
        Returns how many steps the walker has taken
        """
        return self.steps


class Simulation:

    def __init__(self, start, home, seed):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """

        self.start = start
        self.home = home
        self.seed = random.seed(seed)