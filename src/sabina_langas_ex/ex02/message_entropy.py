# -*- coding: utf-8 -*-

from math import log2

__author__ = 'Sabina Langås'
__email__ = 'sabinal@nmbu.no'


def letter_freq(txt):
    """
    This code counts the frequency of the letters in the string that´s entered
    by the user of the code

    :param txt: input for the user of the code, a string

    :return: returns a dictionary where key is the characters in txt and the
             value is the number of occurrences in txt
    """
    freq = {}
    txt_lower = txt.lower()

    for char in txt_lower:
        if char in freq.keys():
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


def entropy(message):
    """
    Returns the calculated entropy (according to information theory)
    of the input message

    :param message: A message that the user want to find the entropy of

    :return: Returns the entropy value for message
    """
    n = len(message)
    message = letter_freq(message)
    h = 0
    for n_i in message.values():
        p_i = n_i/n
        h += -p_i*(log2(p_i))
    return h


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
