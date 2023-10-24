"""My 4th COMP 110 program! Whoohoo!! Practing list utils."""
__author__ = "730658911"

from typing import List


def all(num1: List[int], num2: int) -> bool:
    """Makes sure that that all the numbers in list are the same as a given number."""
    i = 0
    if len(num1) == 0:
        return False
    while i < len(num1):
        if num1[i] == num2:
            i += 1
        else:
            return False
    return True
    

def max(set: list[int]) -> int:
    """Identifies the maximum value in a list."""
    if len(set) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    highV: int = set[0]
    while index < len(set):
        indexC: int = set[index]
        if highV < indexC:
            highV = indexC
        index += 1
    return highV


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determines if one list is equal to another list (same value at same index)."""
    if len(list1) != len(list2):
        return False
    index = 0
    while index < len(list1):
        if list1[index] == list2[index]:
            index += 1
        else:
            return False
    return True
    
