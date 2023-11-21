"""EX06!"""
__author__ = "730318079"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    #"""Rearranging key value pairs."""
    new_dict: dict[str, str] = {}
    for key in dictionary:
        if dictionary[key] in new_dict:
            raise KeyError("You have multiple keys definitions!")
        else:
            new_dict[dictionary[key]] = key
    return new_dict


def favorite_color(color: dict[str, str]) -> str:
    #"""Finding and isolating in a string the color that appears most in the dictionary."""
    fav_color: str = ""
    frequency_colors: dict[str, int] = {}
    for key in color:
        if color[key] not in frequency_colors:
            frequency_colors[color[key]] = 1
        else:
            frequency_colors[color[key]] += 1
    for key in frequency_colors:
        if fav_color == "":
            fav_color = key
        if frequency_colors[key] > frequency_colors[fav_color]:
            fav_color = key
    return fav_color        


def count(number: list[str]) -> dict[str, int]:
    #"""Counting amount a str value appears on list and corresponding the number amount with its string in new dictionary."""
    new_dict_2: dict[str, int] = {}
    count_idx = 0
    while count_idx < len(number) - 1:
        if number[count_idx] not in new_dict_2:
            new_dict_2[number[count_idx]] = 1
        else:
            new_dict_2[number[count_idx]] += 1
        count_idx += 1   
    return new_dict_2


def alphabetizer(alphabet: list[str]) -> dict[str, list[str]]:
    #"""Transforming list of strings to dictionary ordered by strings' first letter."""
    new_dict_3: dict[str, list[str]] = {}
    idx = 0
    while idx < len(alphabet) - 1: 
        if alphabet[idx].lower()[0] not in new_dict_3:
            new_dict_3[alphabet[idx].lower()[0]] = [alphabet[idx]]
        else: 
            new_dict_3[alphabet[idx].lower()[0]].append(alphabet[idx])
        idx += 1
    return new_dict_3


def update_attendance(attendance: dict[str, list[str]], y: str, z: str) -> dict[str, list[str]]:
    #"""Adding string elements into preexisting dictionary."""
    if y in attendance:
        attendance[y].append(z)
    else:
        attendance[y] = [z]
    return attendance