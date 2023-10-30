"""Test my zip function!"""

__author__ = "730658911"

from lessons.zip import zip


def test_empty() -> None:
    """Testing zip with no lists."""
    assert zip([], []) == {}


def test_unequal_lists() -> None:
    """Testing zip of two lists of different lengths (edge case)."""
    x: list[str] = ["walter", "white", "yo"]
    y: list[int] = [1, 2]
    assert zip(x, y) == {}


def test_three_element_list() -> None:
    """Testing zip when a str list and an int list of equal length are provided (use case)."""
    x: list[str] = ["walter", "white", "yo"]
    y: list[int] = [1, 2, 3]
    assert zip(x, y) == {'walter': 1, 'white': 2, 'yo': 3}


def test_two_element_list() -> None:
    """Testing zip of two lists of only one element each (edge case)."""
    x: list[str] = ["walter", "white"]
    y: list[int] = [1, 2]
    assert zip(x, y) == {"walter": 1, "white": 2}