print(r'''
*******************************************************************************
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
ejm97  %%%%

*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
# use a backslash \ for a symbol you want to escape
crossroad = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n')

# you can use .upper() function after variable name to change a variable to uppercase
# or directly after the input prompt text to set the variable to all uppercase
if crossroad.upper() == "LEFT":
    lake = input('You have reached the lake with an island in the middle. '
                 'Type "wait" to wait for a boat or "swim" to swim across.\n').upper()
    if lake == "WAIT":
        house = input('You arrive at the island unharmed. There is a house with 3 doors. '
                      'One red, one blue and one yellow. Which do you choose?\n').upper()
        if house == "YELLOW":
            print("You found the treasure. You Win!")
        elif house == "RED":
            print("You got burned by fire. Game Over.")
        elif house == "BLUE":
            print("You were eaten by beasts. Game Over.")
        else:
            print("That door does not exist. Game Over.")
    else:
       print("You got attacked by a trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
