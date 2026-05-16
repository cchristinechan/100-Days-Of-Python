# exercise 4: BMI calculator
height = 1.65
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)

print(bmi)




# NOTES

# subscripting
print("Hello"[0]) # output = H

print("Hello"[-1]) # specific to python: the -1 means retrieve the last char
# output = o



# datatypes
len("Hello") # outputs for a sized datatype: in this case it is 5
print(type("Hello")) # output: <class 'str'>
print(type(123)) # output: <class 'int'>
print(type(3.14)) # output: <class 'float'>
print(type(True)) # output: <class 'bool'>

# casting
print(int("123") + int("456")) # output = 579

name_of_the_user = input("Enter your name")
length_of_the_name = len(name_of_the_user)
print("Number of letters in your name: " + str(length_of_the_name))

# maths operators
print(123 + 456) # output = 579
print(7 - 3) # output = 4
print(3 * 2) # output = 6
print(5 / 3) # output = 1.6666666666666667
print(5 // 3) # output = 1 (only whole number and gets rid of remainder)
print(2 ** 3) # output = 8 (2 to the power of 3)


# number manipulation + f strings
bmi = 84 / (1.65 ** 2)
print(bmi) # output = 30.85399449035813

print(int(bmi)) # output = 30
print(round(bmi)) # output = 31 (rounds up or down)
print(round(bmi, 2)) # output = 30.85 (rounds to 2 decimal places)

score = 0
score += 2
score -= 1
print(f"Your score is: {score}") # output = Your score is: 1