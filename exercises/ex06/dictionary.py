"""Practice with more dictionaries!"""

__author__ = "730658911"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Returns a new dictionary in which the keys and values are inverted."""
    reversed: dict[str, str] = {}
    for key in x.keys():
        val: str = x[key]
        reversed[val] = key
    
    if len(x) != len(reversed):
        raise KeyError("!!")
    return reversed


def favorite_color(x: dict[str, str]) -> str:
    """Returns the value (color) that occurs most frequently."""
    count: dict[str, int] = {}
    most_loved_color = ""
    max_count: int = 0

    for color in x.values():
        if color in count:
            count[color] += 1
        else:
            count[color] = 1
        if count[color] > max_count:
            most_loved_color = color
            max_count = count[color]
    return most_loved_color


def count(x: list[str]) -> dict[str, int]:
    """Produces a dict from a given list."""
    count: dict[str, int] = {}
    
    for item in x:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Categorizes a list of words into different lists by their first letter."""
    categorized_words: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter in categorized_words:
            categorized_words[first_letter].append(word)
        else:
            categorized_words[first_letter] = [word]
    return categorized_words


def update_attendance(attendance_record: dict[str, list[str]], day: str, student_name: str):
    """Given dict[str, list[str]] will mutate and return the dictionary."""
    if day in attendance_record:
        attendance_record[day] += student_name
    else:
        attendance_record[day] = [student_name]
    return attendance_record