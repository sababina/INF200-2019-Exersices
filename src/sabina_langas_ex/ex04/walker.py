# -*- coding: utf-8 -*-

import random

__author__ = "Sabina Langås"
__email__ = "sabinal@nmbu.no"


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


def walking_home(start, home):
    """
    Handel's the process of walking for start to home

    :param start: The value at where the walker starts
    :param home: The value of where the walker's home is

    :return: How many steps the walker has taken to get home
    """

    walker = Walker(start, home)

    while not walker.is_at_home():
        walker.move()

    return walker.get_steps()


if __name__ == "__main__":

    list_of_distances = [1, 2, 5, 10, 20, 50, 100]
    number_of_simulations = 5
    seed = 1

    random.seed(seed)

    for distance in list_of_distances:
        path_length = [
            walking_home(0, distance)
            for number in range(number_of_simulations)
        ]
        print(
            "Distance: {:3d} -> Path lengths: {}".format(
                distance, sorted(path_length)
            )
        )
