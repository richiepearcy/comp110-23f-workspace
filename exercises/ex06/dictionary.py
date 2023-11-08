"""Exercise 06"""
__author__ = "730318079"

def invert(x: dict[str,str]) -> dict[str, str]:
    new_dict: dict[str,str] = {}
    for key in x:
        if x[key] in new_dict:
            raise KeyError("You have multiple keys definitions!")
        else:
            new_dict[x[key]] = key
    return new_dict

def favorite_color(x: dict[str,str]) -> str:
    fav_color: str = ""
    frequency_colors: dict[str, int] = {}
    for key in x:
        if x[key] not in frequency_colors:
            frequency_colors[x[key]] = 1
        else:
            frequency_colors[x[key]] += 1
    for key in frequency_colors:
        if fav_color == "":
            fav_color = key
        if frequency_colors[key] > frequency_colors[fav_color]:
            fav_color = key
    return fav_color        

def count(x: list[str]) -> dict[str, int]:
    new_dict_2: dict[str, int] = {}
    count_idx = 0
    while count_idx < len(x) - 1:
        if x[count_idx] in new_dict_2:
            new_dict_2[x[count_idx]] += 1
        else:
            new_dict_2[x[count_idx]] = 1   
    return new_dict_2

def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    new_dict_3: dict[str, list[str]] = {}
    idx = 0
    while idx < len(x) - 1: 
        if x[idx].lower()[0] not in new_dict_3:
            new_dict_3[x[idx].lower()[0]] = [x[idx]]
        else: 
            new_dict_3[x[idx].lower()[0]].append(x[idx])
        idx += 1
    return new_dict_3

def update_attendance(x: dict[str,list[str]], y: str, z: str) -> dict[str,list[str]]:
    if y in x:
        x[y].append(z)
    else:
        x[y] = [z]
    return x