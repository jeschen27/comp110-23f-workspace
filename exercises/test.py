"""Dictionary Functions!"""

__author__ = "730658911"

def invert(x: list[str], y: list[str]) -> dict[str, str]:
    '''
    """Inverts the keys and values of two given lists."""
    new_list: dict[str, str] = {y[i]: x[i] for i in range(len(x))}
    for i in x:
        q: int = 0
        for elem in x:
            if new_list[elem] == new_list[i]:
                q += 1
            if q > 1:
                return KeyError
    return new_list
    '''
    """Inverts a dictionary where keys become values and values become keys."""
    """inverted = {}

    for key, value in d.items():

        if value in inverted:

            raise KeyError("Duplicate value encountered while inverting dictionary")

        inverted[value] = key

    return inverted

print(invert(["michael", "jordan", "james"], ["a", "b", "c"]))

def favorite_colors(x: dict[str, str]) -> str:
    counter: int = 0
    color: str = ""
    for elem in x:
        if x[elem] in x:
            counter += 1"""

var: dict[str, int] = {"jack": 1, "jill": 2}
print(var.keys())

"""for i in x[key]:
            q: int = 0
            for elem in x[key]:
                if reversed[elem] == reversed[i]:
                    q += 1
                if q > 1:
                    return KeyError"""

food: dict[str, int] = {"cheese": 1, "eggs": 2, "cheese": 3}
print(food)
# if there are repeat keys in a dictionary, the most recent key's values will override previous ones and
# the length of the dictionary will shorten 