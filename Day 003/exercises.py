# exercise 5: bmi calculator with interpretations
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")


# NOTES
# modulo operator % returns the remainder of a division
# 10 / 3 = 3.33333
# 10 % 3 = 1       because 3 fits into 10 three times with a remainder of 1
# even number % 2 = 0 remainder
