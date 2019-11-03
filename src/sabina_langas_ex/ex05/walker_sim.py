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

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """

        walk = Walker(self.start, self.home)

        while not walk.is_at_home():
            walk.move()

        return walk.steps

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """

        return [self.single_walk() for _ in range(num_walks)]


if __name__ == '__main__':

    print('List 1 to 3 with 20 walks from start at 0 position to home at 10 '
          'position')
    print(f'List 1:{sorted(Simulation(0, 10, 54321).run_simulation(20))}')
    print(f'List 2:{sorted(Simulation(0, 10, 12345).run_simulation(20))}')
    print(f'List 3:{sorted(Simulation(0, 10, 12345).run_simulation(20))}')
    print('List 4 to 6 with 20 walks from start at 10 position to home at 0 '
          'position')
    print(f'List 4:{sorted(Simulation(10, 0, 54321).run_simulation(20))}')
    print(f'List 5:{sorted(Simulation(10, 0, 12345).run_simulation(20))}')
    print(f'List 6:{sorted(Simulation(10, 0, 12345).run_simulation(20))}')