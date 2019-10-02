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

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n // 2] if n % 2 == 1
            else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2]))


def test_median_of_singleton():
    assert median([4]) == 4


def test_median_of_odd_number():
    data =[1, 3, 5, 7, 9]
    assert median(data) == statistics.median(data)