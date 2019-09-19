import numpy as np


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


def entropy(message):
    dist = letter_freq(message)
    su = 0
    for p in dist.values():
        r = p/sum(dist.values())
        if r == 0:
            su += 0
        else:
            su += -r*(np.log(r))
    return su/np.log(2)


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
