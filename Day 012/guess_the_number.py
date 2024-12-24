import art
import random

EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5
lives = 0
end_game = False

print(art.logo)
mystery_number = random.randint(1, 100)

level = input('''Welcome to the number guessing game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': ''').lower()
if level == 'easy':
    lives = EASY_LEVEL_LIVES
else:
    lives = HARD_LEVEL_LIVES

while not end_game:
    print(f"***** Attempts remaining to guess the number: {lives} *****")
    guess = int(input("Make a guess: "))

    # checking whether user has guessed the number yet
    if guess > mystery_number:
        print("Too high.")
    elif mystery_number > guess:
        print("Too low.")
    else:
        print(f"You got it! The answer was {mystery_number}!")
        end_game = True
        break

    # reducing lives by 1 each incorrect guess
    lives -= 1
    if lives > 0:
        print("Guess again.")
    else:
        print("You've run out of guesses. Refresh the page to try again.")
        end_game = True
