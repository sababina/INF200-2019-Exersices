# -*- coding: utf-8 -*-


def letter_freq(txt):
    """
    This code counts the frequency of the letters in the string that´s entered by the user of the code

    Arguments:
        tx {str}: input for the user of the code, a string

    Returns:
         returns a dictionary where key is the characters in txt and the value is the number of occurrences in txt
    """
    freq = {}
    txt_lower = txt.lower()

    for char in txt_lower:
        if char in freq.keys():
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')
    frequencies = letter_freq(text)
    frequencies_sorted = dict(sorted(frequencies.items()))

    for letter, count in frequencies_sorted.items():
        print('{:3}{:10}'.format(letter, count))
