#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay ($150.00 / 5) = 1.12 = 33.60
#Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")

tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

if tip == "10":
    total_bill = float(bill) + (float(bill) * 0.10)
elif    tip == "12":
        total_bill = float(bill) + (float(bill) * 0.12)
elif    tip == "15":
        total_bill = float(bill) + (float(bill) * 0.15)

split_no = input("How many people to split the bill? ")

split_bill = total_bill / float(split_no)
approx_split_bill = "{:.2f}".format(split_bill)
print(f"Each person should pay: ${approx_split_bill}")
