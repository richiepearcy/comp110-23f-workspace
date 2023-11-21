from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
"""EX07."""
__author__: "730318079"


def test_dict_length_1():
    #"""Testing just one pair."""
    test_dict: dict[str, str] = {"North Carolina": "Raleigh"}
    assert invert(test_dict) == {"Raleigh": "North Carolina"}

def test_dict_same_str():
    #"""Testing pair with identical key and value."""
    test_dict: dict[str, str] = {"North Carolina": "North Carolina", "North Carolina": "North Carolina"}
    assert invert(test_dict) == KeyError

def test_dict_length_5():
    #"""Testing multiple key value pairs."""
    test_dict: dict[str, str] = {"North Carolina": "Raleigh", "Virginia": "Richmond", "California": "Sacramento"}
    assert invert(test_dict) == {"Raleigh": "North Carolina", "Richmond": "Virginia", "Sacramento": "California"}

def test_one_color():
    #"""Testing just one repeated color value."""
    test_color_list: dict[str, str] = {"0": "Red", "1": "Red", "2": "Red"}
    assert favorite_color(test_color_list) == "Red"

def test_color_only():
    #"""Testing key value pairs with same color value."""
    test_all_same_color: dict[str, str] = {"Red": "Red", "Red": "Red", "Red": "Red"}
    assert favorite_color(test_all_same_color) == "Red"

def test_two_colors():
    #"""Testing key value pairs with multiple colors."""
    two_colors: dict[str, str] = {"Red": "Yellow", "Yellow": "Red", "Yellow": "Yellow"}
    assert favorite_color(two_colors) == "Yellow"

def test_multiple_same_item():
    #"""Testing list with multiple iterations of one str value."""
    test_list: list[str] = ["Box", "Box", "Box"]
    assert count(test_list) == {"Box": 3}

def test_differing_items():
    #"""Testing list with two different items."""
    test_items: list[str] = ["Box", "Cup", "Cup"]
    assert count(test_items) == {"Box": 1, "Cup": 2}

def test_three_individual_items():
    #"""Testing list with three different items with all different first syllables."""
    test_individual_items: list[str] = ["Box", "Cup", "Phone"]
    assert count(test_individual_items) == {"Box": 1, "Cup": 1, "Phone": 1}

def test_upper_case():
    #"""Testing list with only upper case letter."""
    upper_case_test: list[str] = ["Alpha", "Beta"]
    assert alphabetizer(upper_case_test) == {"a": ["Alpha"], "b": ["Beta"]}

def test_multiple_same_syllable():
    #"""Testing list with items of same first syllable."""
    same_syllable_list: list[str] = ["box", "bucket"]
    assert alphabetizer(same_syllable_list) == {"b": ["Box", "Bucket"]}

def test_same_syllable_not_ordered():
    #"""Testing list with multiple different items of same first syllable."""
    unordered_syllables_list: list[str] = ["cup", "phone", "ceremony"]
    assert alphabetizer(unordered_syllables_list) == {"c": ["cup", "ceremony"], "p": ["phone"]}

def test_not_already_in_dict():
    #"""Testing entering new value in existing key."""
    existing_dict: dict[str, list[str]] = {"phones": ["Android"]}
    new_phone: str = "phones"
    new_type: str = "Apple"
    assert update_attendance(existing_dict, new_phone, new_type) == {"phones": ["Android", "Apple"]}

def test_already_in_dict():
    #"""Testing entering same value in existing key."""
    existing_dict: dict[str, list[str]] = {"phones": ["Android"]}
    new_phone: str = "phones"
    new_type: str = "Android"
    assert update_attendance(existing_dict, new_phone, new_type) == {"phones": ["Android"]}

def test_new_pair():
    #"""Testing new key value pair in existing dict."""
    existing_dict: dict[str, list[str]] = {"phones": ["Android"]}
    new_communication_method: str = "email"
    new_communication_type: str = "Gmail"
    assert update_attendance(existing_dict, new_communication_method, new_communication_type) == {"email": ["Gmail"], "phones": ["Android"]}
