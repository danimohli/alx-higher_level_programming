#!/usr/bin/python3
"""
A function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list of int): A list of unsorted integers.

    Returns:
        int: A peak element from the list.
        A peak element is defined as an element
             that is greater than or equal to its neighbors.

    Notes:
        There may be more than one peak in the list.
        The function returns one of them.

    Complexity:
        The function operates with O(log(n)) complexity,
        using a binary search approach
        to efficiently find a peak element in the list.

    Example:
        >>> find_peak([1, 2, 3, 1])
        3
        >>> find_peak([1, 2, 1, 3, 5, 6, 4])
        2
    """
    if not list_of_integers:
        return None
    
    low, high = 0, len(list_of_integers) - 1
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return list_of_integers[low]
