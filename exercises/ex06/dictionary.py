"""Dictionary Functions!"""

__author__ = "730658911"

def invert(x: list[str], y: list[str]) -> dict[str, str]:
    """Inverts the keys and values of two given lists."""
    """q: int = 0
    current_elem = x[q]
    for i in range(1, len(x)):
        if current_elem == x[i]:
            return KeyError
    else: 
        q += 1"""
        

    return {y[i]: x[i] for i in range(len(x))}

print(invert(["michael", "jordan", "jordan"], ["a", "b", "c"]))

def favorite_color
