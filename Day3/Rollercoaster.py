#Rollercoaster Ticketing
print("Welcome to the roller coaster!!!")
height = int(input("What is your height in centimeters? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age<= 18:
        bill = 7
        print("Teens tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    want_photo = input("Do you want a photo taken? Y or N. ")
    if want_photo == "Y":
        bill += 3

    print(f"Your total bill is {bill}")

else:
    print("You are too short for this ride. You have to grow taller before you can ride.")