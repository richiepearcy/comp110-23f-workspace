"""EX01 Assignment COMP 110"""

__author__ = "730318079"

guessed_word: str = input("Enter a 5-character word: ")
instances: int = 0

if len(guessed_word) != 5:
    print("Error: Word must contain 5 characters")
else: 
    guessed_character: str = input("Enter a single character: ")
    if len(guessed_character) == 1:
        print("Searching for " + guessed_character + " in " + guessed_word)
    else: 
        print("Error: Character must be a single character")
    if guessed_word[0] == guessed_character:
        instances = instances + 1
        print(guessed_character + " found at index 0" )
    if guessed_word[1] == guessed_character:
        instances = instances + 1
        print(guessed_character + " found at index 1")
    if guessed_word[2] == guessed_character:
        instances = instances + 1
        print(guessed_character + " found at index 2")
    if guessed_word[3] == guessed_character:
        instances = instances + 1
        print(guessed_character + " found at index 3")
    if guessed_word[4] == guessed_character:
        instances = instances +1
        print(guessed_character + " found at index 4")
    if instances == 1:
        print(str(instances) + " instance found in " + guessed_word)
    if instances > 1:
        print(str(instances) + " instances found in " + guessed_word)
    if instances == 0:
        print("No instances of "+ guessed_character + " found in " + guessed_word)






