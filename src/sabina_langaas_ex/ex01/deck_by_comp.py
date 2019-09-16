# -*- coding: utf-8 -*-

"""
Solution to task A on exercise 01 in INF200
"""

SUITS = ('C', 'S', 'H', 'D')
VALUES = range(1, 14)


def deck_loop():
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck


def deck_comp():
    return [(suit, val) for suit in SUITS for val in VALUES]


if __name__ == '__main__':
    if deck_loop() != deck_comp():
        print('ERROR!')
    else:
        print('Success')
