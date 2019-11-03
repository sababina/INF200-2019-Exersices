# -*- coding: utf-8 -*-

from walker_sim import Walker, Simulation

__author__ = 'Sabina Langås'
__email__ = 'sabinal@nmbu.no'


class BoundedWalker(Walker):
    """
    Simulates a bounded walk. The walker can not move out of the limits
    that's set.
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
