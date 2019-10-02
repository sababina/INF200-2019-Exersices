# -*- coding: utf-8 -*-

__author__ = 'Sabina Langås'
__email__ = 'sabinal@nmbu.no'


def bubble_sort(data):
    """
    Sorts the data after teh bubble_sort algorithm

    :param data: The data that going to be sort

    :return: Returns the input sorted in a new list
    """
    sort_data = list(data)

    for i in range(len(sort_data) - 1):
        for j in range((len(sort_data) - 1 - i)):
            if sort_data[j] > sort_data[j + 1]:
                sort_data[j], sort_data[j + 1] = sort_data[j + 1], sort_data[j]
    return sort_data


def test_empty():
    """Test that the sorting function works for empty list"""
    empty_list = []
    assert empty_list == bubble_sort(empty_list)


def test_single():
    """Test that the sorting function works for single-element list"""
    single_element_list = [1]
    assert single_element_list == bubble_sort(single_element_list)


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data != sorted_data


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data == [3, 2, 1]


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [1, 2, 3]
    sorted_data = bubble_sort(data)
    assert sorted_data == data


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [5, 4, 3, 2, 1]
    sorted_data = sorted(data)
    assert sorted_data == bubble_sort(data)


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data = [2, 5, 3, 2, 7, 5]
    sorted_data = sorted(data)
    assert sorted_data == bubble_sort(data)


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    pass
