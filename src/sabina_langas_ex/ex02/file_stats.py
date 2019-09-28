# -*- coding: utf-8 -*-

__author__ = 'Sabina Langås'
__email__ = 'sabinal@nmbu.no'


def char_counts(textfilename):
    """
    Opens given file and reads it to one single string.
    Counts how often each character code occurs int the string and
    return the result as a list or tuple.

    :param textfilename: The textfile you want to analyse

    :return: Returns a list or tuple of counted character code
    """
    open_file = open(textfilename, encoding='utf-8')
    content_of_file = open_file.read()
    result = [0]*256

    for char in content_of_file:
        result[ord(char)] += 1
    return result


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
