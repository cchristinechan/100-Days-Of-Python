print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))

percentage = tip/100 + 1
total_per_person = ("{:.2f}".format((bill/people * percentage))) # formatted to a string
print(f"Each person should pay: ${total_per_person}")
