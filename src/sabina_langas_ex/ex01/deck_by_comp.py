# -*- coding: utf-8 -*-


SUITS = ('C', 'S', 'H', 'D')
VALUES = range(1, 14)


def deck_loop():
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck


def deck_comp():
    """
    Creates a deck of cards and returns it
    
    Returns:
        list -- List of tuples of the form (suit: str, val: int)
    """    
    return [(suit, val) for suit in SUITS for val in VALUES]


if __name__ == '__main__':
    if deck_loop() != deck_comp():
        print('ERROR!')
    else:
        print('Success')
