import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if 0 <= player_choice < 3: # in range
    print("You chose: " + images[player_choice])

computer = random.randint(0, 2)
print("Computer Chose:" + images[computer])

if player_choice >= 3 or player_choice < 0: # out of range
    print("You typed an invalid number. You lose!")
elif player_choice == 0 and computer == 2: # you play rock, computer plays scissors
    print("You win!")
elif computer == 0 and player_choice == 2: # computer plays rock, you play scissors
    print("You lose!")
elif computer == player_choice:
    print("It is a draw")
elif computer > player_choice: # paper beats rock, scissors beats paper
    print("You lose!")
elif player_choice > computer: # paper beats rock, scissors beats paper
    print("You win!")
