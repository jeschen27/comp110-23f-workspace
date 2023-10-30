"""Combining two lists into a dictionary."""
__author__ = "730658911"


def zip(x: list[str], y: list[int]) -> dict[str, int]: 
    """Creates a dictionary that assignes the element of one list to the element of another list at the same index."""
    if len(x) != len(y):
        return {}
    if not x:
        return {}
    
    return {x[i]: y[i] for i in range(len(x))}