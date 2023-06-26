#SUb-topic......Type Error: 'Cause int has no length, Only strings.
# print(len(123))

#Type Conversion(Type Casting): Convert int to string to be able to concatenate

# num_char = len(input("What is your name? "))

#Convert Type 'int' to 'string'
# new_num_char = str(num_char)

# print("Your name has " + new_num_char + " characters.")

#Write a program that adds any two random numbers collected from user input


#Sub-Topic.......Interactive Coding Exercises
#from unittest import result


#two_digit_number = input("Type a two digit number: ")

#first_digit = int(two_digit_number[0])
#second_digit = int(two_digit_number[1])
#result = first_digit + second_digit

#print(result)

"""#BMI calculator...... weight(kg)/height^2(m^2)
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

(BMI) = int(weight) / (float(height) ** 2)

bmi_as_int = int(BMI)

print(bmi_as_int)

#F-String Conversion

print(f"Your BMI is {bmi_as_int}") """

""" #Day 2.3 - Your life in weeks
age = input("What is your current age? ")


# 365days = 1yr, 52weeks = 1yr, 12months = 1yr
# Say you can live up to 90yrs, how many days, weeks and months will be left of your life??

age_left = 90 - int(age)
days_left = age_left * 365
weeks_left = age_left * 52
months_left = age_left * 12

message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message) """