import random
from colorama import Fore, Style

with open ("wordlewords.txt", "r") as file:
    word_list = file.read().splitlines()
print("\nWelcome to Vocabmaxx!\n")
print("You have 6 guesses to guess the 5 letter word. If you guess correct, you win!\n")


secret_word = random.choice(word_list).upper().strip()

for guess in range(1,7):
    display = ""
    letter_counts = {}
    user_guess = ""
    while len(user_guess) != 5:
        user_guess = input(f"Guess {guess}:").upper().strip()
        if len(user_guess) != 5:
            print("\033[F\033[K", end="")
            user_guess = "" 
    print("\033[F\033[K", end="")
    
    for i, letter in enumerate(user_guess):
        if secret_word[i] == letter:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1

    for i, letter in enumerate(user_guess):
        if secret_word[i] == letter:
            display += Fore.GREEN + letter + Style.RESET_ALL + " "


        elif letter in secret_word:
            actual_count = secret_word.count(letter)
            used_so_far = letter_counts.get(letter, 0)

            if used_so_far < actual_count:
                display += Fore.YELLOW + letter + Style.RESET_ALL + " "
                letter_counts[letter] = used_so_far + 1

            else:
                display += letter + " "
        else:
            display += letter + " "

    print(display)

    
    if user_guess == secret_word:
        print("\nCongrats! You win!")
        break
    display = ""
if user_guess != secret_word:
    print("\nBetter luck next time!")
    print(f"\nThe word was {secret_word}")
   

