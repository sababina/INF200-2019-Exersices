# -*- coding: utf-8 -*-

"""
Solution to task D exercise 01 in INF200
"""

from random import randint

__author__ = 'Sabina Langås'
__email__ = 'sabinal@nmbu.no'

""" 
    This is a game were you try to guss a number of the roll of two dices.
    You get 3 attempts at guessing, and you earn points as following:
    -First attempt right 3 points
    -Second attempt right 2 points
    -Third attempt right 1 point
"""


def get_valid_input():
    """  Get a integer input > 0 from user

    :return: int -- input
    """
    guess = 0
    while guess < 1:
        guess = int(input('Your guess between 2 and 12: '))
    return guess


def roll_dice(die_low, die_high) -> int:
    """ Return the sum of two dice rolls.

    :param die_low: lowest number on dice
    :param die_high: highest number on dice

    :return: gives the sum of to dice rolls
    """
    return randint(die_low, die_high) + randint(die_low, die_high)


def correct_guess(correct: int, guess: int) -> bool:
    """ Returns true if the answer is right, returns false otherwise

    :param correct: correct answer
    :param guess: user guess

    :return bool: correct answer or not
    """
    return correct == guess


if __name__ == '__main__':

    DIE_LOW: int = 1
    DIE_HIGH: int = 6

    guessed_correct = False
    remaining_attempts = 3
    correct_answer = roll_dice(DIE_LOW, DIE_HIGH)  # type: int

    while not guessed_correct and remaining_attempts > 0:
        user_guess = get_valid_input()
        guessed_correct = correct_guess(correct_answer, user_guess)

        if not guessed_correct:
            print('Wrong, try again!')
            remaining_attempts -= 1

    if remaining_attempts > 0:
        print(f'You won {remaining_attempts} points.')
    else:
        print(f'You lost. Correct answer: {correct_answer}.')
