# pizza order
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium/large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
# work out how much they need to pay based on their size choice
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")

# work out how much to add to their bill based on their pepperoni choice.
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# work out their final amount based on whether if they want extra cheese.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")