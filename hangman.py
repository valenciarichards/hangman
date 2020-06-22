# Import the random, string and natural language toolkit modules.
import random
import string
from nltk.corpus import words


# Create a function to play hangman
def play_hangman():

    # Randomly pick a secret word that has 4 or more letters.
    word_list = words.words()
    secret_word = ""
    while len(secret_word) < 4:
        secret_word = random.choice(word_list)
    # Put a '_' in the display word for every letter that needs to be guessed.
    display_word = ["_"] * len(secret_word)
    guessed_letters = []
    tries_left = 8

    while tries_left > 0 and "_" in display_word:
        # Show the player which letters have (and haven't) been guessed, and the number of tries that are left.
        print("\n" + "".join(display_word))
        if tries_left == 1:
            print("\nYou have 1 try left")
        else:
            print("\nYou have", tries_left, "tries left")
        letter_guess = input("Guess a letter: ")
        # If the guess is invalid, restart the loop.
        if len(letter_guess) != 1:
            print("Please guess a single letter.")
            continue
        if letter_guess not in string.ascii_letters:
            print("That is not a letter.")
            continue
        if letter_guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        # Add all valid guesses to a list of letters guessed.
        else:
            guessed_letters.append(letter_guess)
        # Update the display word if the player guesses a letter correctly.
        if letter_guess in secret_word:
            for x, letter in enumerate(secret_word):
                if letter_guess == letter:
                    display_word[x] = letter_guess.upper()
        # If the letter isn't in the secret word, tell the player and subtract 1 from their remaining guesses.
        else:
            print("That letter is not in the word.")
            tries_left -= 1

    # If the player guesses all the letters in the secret word before running out of guesses, they win!
    if "_" not in display_word:
        print("\nYou guessed the word \"" + secret_word.upper() + "\"!\nYou win!")
    else:
        print("\nYou didn't guess the word \"" + secret_word.upper() + "\"!\nYou lose!")


# Display a welcome menu.
while True:
    print('''
    H A N G M A N

    "play"  : Play a game
    "exit"  : Quit the program
    ''')
    choice = input("\nWhat would you like to do? ")
    if choice == "play":
        print("\nGood luck!")
        play_hangman()
        continue
    elif choice == "exit":
        quit()
    else:
        print("Please choose from the options above.")
        continue
