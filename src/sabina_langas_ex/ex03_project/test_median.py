# -*- coding: utf-8 -*-

import pytest

__author__ = "Sabina Langås"
__email__ = "sabinal@nmbu.no"


def median(data):
    """
    The median code is collected from yngvem(github user) :
    https://github.com/yngvem/INF200-2019-Exercises.git

    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """
    sorted_data = sorted(data)
    num_elements = len(sorted_data)

    if num_elements % 2 == 1:
        return sorted_data[num_elements // 2]
    elif not sorted_data:
        raise ValueError("Please insert a list that is not empty")
    else:
        return (
            sorted_data[num_elements // 2 - 1] + sorted_data[num_elements // 2]
        ) / 2


def test_median_of_single_element_list():
    """ Test that median function works for a one-element list."""
    assert median([4]) == 4


def test_median_of_odd_number():
    """ Test that median function works for a list with odd numbers of
    elements."""
    data = [1, 3, 5, 7, 9]
    assert median(data) == 5


def test_median_of_even_numeber():
    """ Test that median function  works for a list with even numbers of
    elements."""
    data = [2, 4, 6, 8, 10]
    assert median(data) == 6


def test_median_of_ordred_list():
    """ Test that median function works for a list with ordered elements."""
    data = [1, 2, 3, 4, 5]
    assert median(data) == 3


def test_median_of_reverse_ordred_list():
    """ Test that median function works for a list with reverse-ordered
    elements."""
    data = [5, 4, 3, 2, 1]
    assert median(data) == 3


def test_median_of_unsorted_list():
    """ Test that median function works for a list with unordered elements."""
    data = [2, 6, 3, 9, 13]
    assert median(data) == 6


def test_median_raises_value_error_on_empty_list():
    """ Test that median function raises a ValueError exception for an empty
    list."""
    with pytest.raises(ValueError):
        median([])


def test_original_data_stays_same():
    """ Test that median function leaves the original data unchanged."""
    data = [1, 2, 3]
    median(data)
    assert data == [1, 2, 3]


def test_median_of_tuple_works():
    """ Test that median function works for tuples as well as lists."""
    list1 = [1, 2, 3, 4]
    tuple1 = tuple(list1)
    assert median(list1) == 2.5
    assert median(tuple1) == 2.5
