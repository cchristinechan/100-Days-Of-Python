from game_data import data
import random
from art import logo,vs

score = 0
end_game = False

def format_data(account_num):
    """Takes in the account number and returns a formatted string of the account name, description and country of origin."""
    return(f"{data[account_num]["name"]}, a {data[account_num]["description"]}, "
            f"from {data[account_num]["country"]}.")


def correct_guess(a, b, user_guess):
    """Takes in account a, b and user guess and returns a formatted string stating
    if the user correctly guessed the higher follower count."""
    higher_account = ''
    global score
    global end_game
    if a > b:
        higher_account = 'a'
    else:
        higher_account = 'b'

    if higher_account == user_guess:
        score += 1
        return f"You're right! Current score: {score}"
    else:
        end_game = True
        return f"Sorry, that's wrong. Final score: {score}"


print(logo)
account_a = random.choice(data)
while not end_game:
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    account_a_follower_count = data[account_a]["follower_count"]
    account_b_follower_count = data[account_b]["follower_count"]

    print("\n" * 20 + logo)
    print(correct_guess(account_a_follower_count, account_b_follower_count, guess))
    account_a = account_b
