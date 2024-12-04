# GLORY BE TO GOD,
# NUMBER GUESSING GAME,
# BY ISRAEL MAFABI EMMANUEL

import random

import os
import sys
import platform

def game(number:int, attempts:int)->None:
    """
    The main game function where the user guesses the number
    :param number:(int) The number to be guessed.
    :param attempts:(int) The number of attempts left.
    :return: The function returns None... a void function.
    """
    if attempts <= 0:
        print(f"message: You Lose! the correct guess was: {number}")
        start()
    else:
        while True:
            try:
                user_number: int = int(input("message: make a guess, what's the number? "))  # user's guess...🤭
                break
            except ValueError:
                print("Invalid input, Please enter a number.")

        if user_number == number:
            print("message: Oh my... You Win! - what a champ!")
            start()
        elif user_number > number:
            attempts -= 1
            print("message: Oh boy!... that's too Big!")
            print(f"message: attempts remaining: {attempts}")
            game(number, attempts)
        elif user_number < number:
            attempts -= 1
            print("message: Oh brother!... that's too small though!")
            print(f"message: attempts remaining: {attempts}")
            game(number, attempts)

def start()->bool:
    """
    The start function to select the game level and initiate the game.
    :return bool: The function returns True if the game should restart, False to exit.
    """
    print("----- Welcome to Mafabi's Guessing Game!!! -----")
    print("Select Game Level: ")
    print("1) Easy          [0 - 20 ]")
    print("2) Medium        [0 - 60 ]")
    print("3) Medium Hard   [0 - 100]")
    print("4) Hard          [0 - 250]")
    print("5) Clear Screen  [ num 5 ]")
    print("Otherwise, press any numeric key above or below selections to exit...")
    while True:
        try:
            selection: int = int(input("Select Level: "))  # user selection on the main menu...
            break
        except ValueError:
            print("Invalid input, Please enter a number.")

    random_limit:int | None = {
        1: 20,
        2: 60,
        3: 100,
        4: 250
    }.get(selection, None)

    if selection == 5:
        if platform.system() == "Windows":
            os.system('cls') # clear the screen - Windows
        else:
            os.system('clear') # clear the screen - macOS and Linux
        return True

    if random_limit is None:
        print("Goodbye!")
        sys.exit()

    # function for generating the random number...
    def generate(limit: int)->int:
        return random.randint(0, limit)

    attempts:int = 5
    random_number = generate(random_limit)
    game(random_number, attempts)
    return True

def main():
    while start():
        pass # Loop the game if start returns true...

if __name__ == "__main__":
    main()