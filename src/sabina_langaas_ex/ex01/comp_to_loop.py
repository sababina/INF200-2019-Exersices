# -*- coding: utf-8 -*-


def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    """Returns a list containing the squares of all factors of 3 up to n
    
    Arguments:
        n {int} -- Integer which the for loop will count up to
    
    Returns:
        list -- list including the squares
    """    
    square_list= []
    
    for k in range(n):
        if k % 3 == 1:
            squares.append(k**2)
    return squares


if __name__ == '__main__':
    if squares_by_comp(number) != squares_by_loop(number):
        print('ERROR!')
