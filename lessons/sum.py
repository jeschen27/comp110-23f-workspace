"""Summing the elements of a list using different loops."""
__author__ = "730658911"


def w_sum(vals: list[float]) -> float:
    """Adds up all the elements in a list using a while loop."""
    idx = 0
    sum = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Adds up all the elements in a list using a for ... in ... loop."""
    sum = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Adds up all the elements in a list using a for ... in range(...) loop."""
    sum = 0.0
    for idx in range(0, len(vals)): 
        sum += vals[idx]
    return sum
