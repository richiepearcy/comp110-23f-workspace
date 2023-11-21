from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
"""EX07."""
__author__: "730318079"


def test_dict_length_1():
    test_dict: dict[str, str] = {"North Carolina": "Raleigh"}
    assert invert(test_dict) == {"Raleigh": "North Carolina"}

def test_dict_same_str():
    test_dict: dict[str, str] = {"North Carolina": "North Carolina", "North Carolina": "North Carolina"}
    assert invert(test_dict) == KeyError

def test_dict_length_5():
    test_dict: dict[str, str] = {"North Carolina": "Raleigh", "Virginia": "Richmond", "California": "Sacramento"}
    assert invert(test_dict) == {"Raleigh": "North Carolina", "Richmond": "Virginia", "Sacramento": "California"}

def test_one_color():
    test_color_list: dict[str, str] = {"0": "Red", "1": "Red", "2": "Red"}
    assert favorite_color(test_color_list) == "Red"

def test_color_only():
    test_all_same_color: dict[str, str] = {"Red": "Red", "Red": "Red", "Red": "Red"}
    assert favorite_color(test_all_same_color) == "Red"

def test_two_colors():
    two_colors: dict[str, str] = {"Red": "Yellow", "Yellow": "Red", "Yellow": "Yellow"}
    assert favorite_color(two_colors) == "Yellow"

def test_multiple_same_item():
    test_list: list[str] = ["Box", "Box", "Box"]
    assert count(test_list) == {"Box": 3}

def test_differing_items():
    test_items: list[str] = ["Box", "Cup", "Cup"]
    assert count(test_items) == {"Box": 1, "Cup": 2}

def test_three_individual_items():
    test_individual_items: list[str] = ["Box", "Cup", "Phone"]
    assert count(test_individual_items) == {"Box": 1, "Cup": 1, "Phone": 1}

def test_upper_case():
    upper_case_test: list[str] = ["Alpha", "Beta"]
    assert alphabetizer(upper_case_test) == {"a": ["Alpha"], "b": ["Beta"]}

def test_multiple_same_syllable():
    same_syllable_list: list[str] = ["box", "bucket"]
    assert alphabetizer(same_syllable_list) == {"b": ["Box", "Bucket"]}

def test_same_syllable_not_ordered():
    unordered_syllables_list: list[str] = ["cup", "phone", "ceremony"]
    assert alphabetizer(unordered_syllables_list) == {"c": ["cup", "ceremony"], "p": ["phone"]}

