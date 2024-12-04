# Mafabi's Guessing Game

## Overview

Mafabi's Guessing Game is a simple number-guessing game where the user attempts to guess a randomly generated number within a specified range. The game offers multiple difficulty levels and provides feedback on whether the guesses are too high or too low.

## How to Play

1. Select a difficulty level.
2. Make guesses to find the randomly generated number within the allowed attempts.
3. Receive feedback on whether your guess is too high or too low.
4. Win by guessing the number correctly within the allowed attempts or lose if you run out of attempts 🤭😉.

## Functions and Logic

### `game(number: int, attempts: int) -> None`

**Purpose:** This function handles the main game logic where the user attempts to guess the number. It checks if the user has any attempts left and provides feedback on each guess.

**Parameters:**

- `number` (int): The number to be guessed.
- `attempts` (int): The number of attempts left.

**Logic:**
- If attempts are exhausted (`attempts <= 0`), the user loses and the correct number is revealed.
- If the user guesses the correct number, a winning message is displayed.
- If the guess is incorrect, feedback is given on whether the guess is too high or too low, and the number of remaining attempts is updated.

### `start() -> bool`

**Purpose:** This function initializes the game by allowing the user to select a difficulty level and generates the random number to be guessed. It also handles the option to clear the screen.

**Returns:** `bool` - True if the game should restart, False to exit.

**Logic:**
- Displays the game levels and instructions to the user.
- Takes user input to select the game level or clear the screen.
- Based on the selected level, sets the random number limit.
- Generates the random number within the set limit.
- Starts the `game` function with the generated number and a fixed number of attempts.

### `generate(limit: int) -> int`

**Purpose:** This function generates a random number within a specified limit.

**Parameters:**
- `limit` (int): The upper limit for the random number generation.

**Returns:** `int` - A randomly generated number within the specified limit.

### `main() -> None`

**Purpose:** The main function to run the game loop. It keeps the game running as long as the user wants to continue playing.

**Logic:**
- Calls the `start` function within a loop to keep the game running.
- If `start` returns True, the game restarts; if False, the game exits.

## Compilation Instructions

### Windows

1. Install `pyinstaller` if not already installed:

   ```shell
   pip install pyinstaller # pyinstaller installation...
   ```

2. Create an executable using `pyinstaller`:

   ```shell
   pyinstaller --onefile --windowed main.py # creating the windows executable...
   ```

3. Locate now your created executable... on your project folder.

### Unix (Linux/macOS)

1. Add the **Shebang** line at the top of the main.py

   ```python
   #!/usr/bin/env python3
   # This just tells the system to use the python interpreter to run the script...
   ```

2. Making the script executable, change the file permissions to make it executable... That is by opening your terminal and navigate to the directory containing your script. Then run:

   ```shell
   chmod +x main.py #making the executable
   ```

3. Then run the script, you can now run it directly from the terminal by typing:

   ```shell
   ./main.py
   ```

4. Alternatively you can pursue still using - `pyinstaller`.

   

### **Enjoy the Game!!!**

Feel free to reach out... 🤭😍😉

Made with Love... ~ Happy Guessing 😎

More so, Glory to God!!! ~ Jesus is Lord!