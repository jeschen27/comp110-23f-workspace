"""Dict Unit Tests!"""
from dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest

__author__ = "730658911"


# invert function
def test_normal() -> None:
    """Testing a dictionary with unique str keys and values."""
    favorite_color: dict[str, str] = {"Jack": "red", "Cesar": "orange", "Jessica": "blue"}
    assert invert(favorite_color) == {"red": "Jack", "orange": "Cesar", "blue": "Jessica"}


def test_repeat() -> None:
    """Testing a dictionary with repeat keys in the new inverted dictionary.""" 
    with pytest.raises(KeyError):
        favorite_food: dict[str, str] = {"Jack": "steak", "Cesar": "steak", "Jessica": "chocolate"} 
        invert(favorite_food)


def test_one_pair() -> None:
    """Testing a dictionary with only one key-value pair."""
    my_friends: dict[str, str] = {"Eva": "my homie"}
    assert invert(my_friends) == {"my homie": "Eva"}


# favorite_color
def test_favs() -> None:
    """Testing a dictionary with two people (keys) having the same favorite color (value)."""
    fav_colors: dict[str, str] = {"Jack": "red", "Arav": "red", "Jessica": "blue"}
    assert favorite_color(fav_colors) == "red"


def test_unique_colors() -> None:
    """Testing a dictionary with unique keys and values. Everyone has a different favorite color."""
    fav_colors: dict[str, str] = {"Jack": "red", "Cesar": "orange", "Jessica": "blue"}
    assert favorite_color(fav_colors) == "red"
    

def test_empty_dict() -> None:
    """Testing an empty dictionary."""
    fav_colors: dict[str, str] = {}
    assert favorite_color(fav_colors) == ""


# count
def test_unique_types_of_cookies() -> None:
    """Testing a list of strings with unique elements."""
    cookies: list[str] = ["chocolate chip", "oatmeal", "sugar", "red velvet"]
    assert count(cookies) == {"chocolate chip": 1, "oatmeal": 1, "sugar": 1, "red velvet": 1}


def test_repeat_types_of_cookies() -> None:
    """Testing a list of strings with repeat elements."""
    cookies: list[str] = ["chocolate chip", "chocolate chip", "red velvet", "oatmeal", "red velvet", "sugar", "red velvet"]
    assert count(cookies) == {"chocolate chip": 2, "red velvet": 3, "oatmeal": 1, "sugar": 1}


def test_no_cookies() -> None:
    """Testing an empty list."""
    cookies: list[str] = []
    assert count(cookies) == {}


# alphabetizer
def test_three_tasty_foods() -> None:
    """Testing a list of three strings with two strings that start witht the same letter."""
    tasty_foods: list[str] = ["steak", "chocolate", "cheesecake"]
    assert alphabetizer(tasty_foods) == {"c": ["chocolate", "cheesecake"], "s": ["steak"]}
    

def test_tasty_foods_with_same_letter() -> None:
    """Testing a list with three strings that all begin with the same letter."""
    tasty_foods: list[str] = ["pasta", "peanuts", "potatoes"]
    assert alphabetizer(tasty_foods) == {"p": ["pasta", "peanuts", "potatoes"]}


def test_no_tasty_foods() -> None:
    """Testing an empty list."""
    tasty_foods: list[str] = []
    assert alphabetizer(tasty_foods) == {}


# update_attendance
def test_attendance_this_week() -> None:
    """Testing adding an additional key-value pair to a dictionary."""
    attendance: dict[str, list[str]] = {"monday": ["Jane", "Ryan"]}
    assert update_attendance(attendance, "tuesday", "Bobby") == {"monday": ["Jane", "Ryan"], "tuesday": ["Bobby"]}


def test_no_attendance_some_days() -> None: 
    """Testing adding a key-value pair with the value being empty to a dictionary."""
    attendance: dict[str, list[str]] = {"monday": [""], "tuesday": ["Paul", "Gayatri"]}
    assert update_attendance(attendance, "wednesday", "") == {"monday": [""], "tuesday": ["Paul", "Gayatri"], "wednesday": [""]}


def test_forgot_attendance() -> None:
    """Testing adding an empty key-value pair."""
    attendance: dict[str, list[str]] = {}
    assert update_attendance(attendance, "", "") == {"": [""]}