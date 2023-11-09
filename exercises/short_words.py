"""Quiz 2 practice."""

__author__ = "730658911"


def short_words(my_list: list[str]) -> list[str]:
    """Returns a new list including only the input elements that are less than 5 characters."""
    new_list: list[str] = []
    for elem in my_list:
        if len(elem) < 5:
            new_list += elem
        else:
            print(f"{elem} is too long!")
    return new_list