"""EX02 Assignment COMP 110"""
__author__ = "730318079"

secret_word: str = "knoll"
secret_word_length: int = len(secret_word)
guessed_word: str = input(f"What is your { secret_word_length }-letter guess? ")
guessed_word_length: int = len(guessed_word)

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

emoji: str = ""
idx: int = 0

while idx < secret_word_length:
    if guessed_word_length == secret_word_length:
        # If guess is same length as secret word, continue checking
        if guessed_word[idx] == secret_word[idx]:
            # if first letter of guess matches first letter of secret word, print a green box and continue checking other letters
            emoji = emoji + GREEN_BOX
            idx += 1
        else:
            # If letters don't match, check to see if letter in guess is anywhere else in secret word
            comparison = False
            alternate_idx = 0
            while comparison is False and alternate_idx < secret_word_length:
                if secret_word[alternate_idx] == guessed_word[idx]:
                    # If guessed letter is found in another index of secret word, change boolean to True to print yellow box
                    comparison = True
                else:
                    # if guessed letter is not found at that index, keep checking other index's
                    alternate_idx += 1
            if comparison is True:
                # Yellow box is printed for that letter if is located at a different index in secret word, and then move on to check other letters
                emoji = emoji + YELLOW_BOX 
                idx += 1 
            else:
                # White box is printed for that letter if not located at all in secret word, and then move on to check other letters
                emoji = emoji + WHITE_BOX    
                idx += 1
    else: 
        # If guess is not same length as secret word, inform them to try again
        print(f"That was not a { secret_word_length }-letter guess!")
        exit()
if guessed_word == secret_word:
    # If they guess correctly, inform them
    print(emoji)
    print("Woo! You got it!")
else:
    # If they guess incorrectly, inform them
    print(emoji)
    print("Not quite. Play again soon!")
    exit()