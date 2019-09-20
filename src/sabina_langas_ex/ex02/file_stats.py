# -*- coding: utf-8 -*-


def char_counts(textfilename):
    open_file = open(textfilename, encoding='utf-8')
    content_of_file = open_file.read()
    result = [0]*256

    converted_file = [ord(letters) for letters in content_of_file]

    for number in range(len(converted_file)):
        for char_number in range(256):
            if converted_file[number] == char_number:
                result[char_number] += 1
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
