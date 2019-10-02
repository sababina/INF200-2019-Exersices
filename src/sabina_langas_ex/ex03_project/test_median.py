# -*- coding: utf-8 -*-

import statistics
import pytest

__author__ = 'Sabina Langås'
__email__ = 'sabinal@nmbu.no'


def median(data):
    """
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
        )/2


def test_median_of_singleton():
    assert median([4]) == 4


def test_median_of_odd_number():
    data = [1, 3, 5, 7, 9]
    assert median(data) == statistics.median(data)


def test_median_of_even_numeber():
    data = [2, 4, 6, 8, 10]
    assert median(data) == statistics.median(data)


def test_median_of_ordred_list():
    data = [1, 2, 3, 4, 5]
    assert median(data) == statistics.median(data)


def test_median_of_reverse_ordred_list():
    data = [5, 4, 3, 2, 1]
    assert median(data) == statistics.median(data)


def test_median_of_unsorted_list():
    data = [2, 6, 3, 9, 13]
    assert median(data) == statistics.median(data)


def test_median_raises_value_error_on_empty_list():
    with pytest.raises(ValueError):
        median([])
    pass


def test_original_data_stays_same():
    data = [1, 2, 3]
    median(data)
    assert data == [1, 2, 3]


def test_median_of_tuple_works():
    list1 = [1, 2, 3, 4]
    tuple1 = tuple(list1)
    assert median(list1) == median(tuple1)
