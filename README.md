# Vocabmaxx

Vocabmaxx is a terminal based clone of the popular game Wordle, built entirely on Python. 

## Features

- **Terminal Color Feedback:** Uses `colorama` to provide instant Green/Yellow/Grey visual feedback after each guess.
- **Dynamic Input Validation:** Ensures players can only enter valid 5-letter guesses. If a user enters an incorrect word length, the game automatically clears the bad line using ANSI escape codes (`\033[F\033[K`) to keep the interface looking pristine.
- **Advanced Letter Tracking:** Implements a dictionary-based tracking system and a two-phase pre-scan loop. This eliminates the classic single-loop Wordle bug, ensuring that duplicate letters are colored accurately (e.g., preventing a yellow letter from "stealing" a hint from a perfect green match further down the word).

## How It Works: The Duplicate Letter Algorithm

A common challenge in creating a wordle-like game is handling duplicate letters properly. For example, if the word is APPLE, and the user enters APLLE, due to the nature of reading from left to right, a loop will view the first L and mark it as correct but in the wrong spot (yellow) even though the next L is in the correct spot (green). This confuses the user into thinking that there are two Ls in the word, even though APPLE only has one.

Here is how I overcame this challenge:

### 1. The Pre-Scan 
The program loops through the user's guess and compares it to the correct word, before displaying a result with colored letters. This pre-scan counts and collects all the correct index matches (**Greens**) into a `letter_counts` dictionary.

### 2. The Main Loop 
As it prints the display from left to right, the loop checks the 'letter_counts' dictionary. Each letter is checked at first to see if its index in the user's guess matches that of the actual word. If so, the letter is marked as green. Else, if the number of occurances of a letter in the user's guess (tracked in 'letters_count') is less than the actual number of occurances, then the letter is marked as yellow. If not, then it is marked as grey. 

## Requirements and Installation

Before you play, have Python installed and the 'colorama' library downloaded.

1. Clone or download this repository.
2. Have your word list file ('wordlewords_txt') saved in the same folder as the script. 
3. Install the required dependency via terminal:
   ```bash
   pip install colorama
