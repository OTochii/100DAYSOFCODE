from telnetlib import BM


height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

(BMI) = int(weight) / (float(height) ** 2)

bmi_as_int = int(BMI)

print(bmi_as_int)

if BMI < 18.5:
    print("You're Underweight.")
elif BMI > 18.5 and BMI < 25:
    print("You have a Normal Weight.")
elif BMI > 25 and BMI < 30:
    print("You are Overweight.")
elif BMI > 30 and BMI < 35:
    print("You are Obese.")
else:
    print("You are clinically Obese.")
