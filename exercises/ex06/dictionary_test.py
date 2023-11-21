"""EX07."""
__author__: "730318079"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance

def test_dict_length_1():
    test_dict: dict[str, str] = {"North Carolina": "Raleigh"}
    assert invert(test_dict) == {"Raleigh": "North Carolina"}

def test_dict_same_str():
    test_dict: dict[str, str] = {"North Carolina": "North Carolina", "North Carolina": "North Carolina"}
    assert invert(test_dict) == KeyError

