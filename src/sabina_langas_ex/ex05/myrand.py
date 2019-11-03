# -*- coding: utf-8 -*-

from walker_sim import Walker, Simulation

__author__ = 'Sabina Langås'
__email__ = 'sabinal@nmbu.no'


class BoundedWalker(Walker):
    """
    Simulates a bounded walk. The walker of the walk can not move out of the
    limits that's set.
    """

    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """

        super().__init__(start, home)
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.x = self.x

    def move(self):

        super().move()
        if self.x < self.left_limit:
            self.x = self.left_limit
        elif self.x > self.right_limit:
            self.x = self.right_limit


class BoundedSimulation(Simulation):
    """
    Simulates one or more bounded walks. The walker of the walk  can not move
    out of the limits that's set.
    """

    def __init__(self, start, home, seed, left_limit, right_limit):
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
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """

        super().__init__(start, home, seed)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def single_walk(self):

        """
        Simulates on single bounded walk

        :return:
            Number of steps taken
        """

        walker = BoundedWalker(self.start, self.home,
                               self.left_limit, self.right_limit)

        num_steps = 0

        while not walker.is_at_home():
            walker.move()
            num_steps += 1

        return num_steps
