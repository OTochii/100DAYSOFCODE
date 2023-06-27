print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower_case = name1.lower()
#print(name1_lower_case)
name2_lower_case = name2.lower()
#print(name2_lower_case)

#Check how many times "TRUE" and "LOVE" occurs in name1 and name2

#Combine both names

name_combo = name1_lower_case + name2_lower_case
t_occurs = name_combo.count("t")
r_occurs = name_combo.count("r")
u_occurs = name_combo.count("u")
e_occurs = name_combo.count("e")
True_occurs = t_occurs + r_occurs + u_occurs + e_occurs
print(True_occurs)

l_occurs = name_combo.count("l")
o_occurs = name_combo.count("o")
v_occurs = name_combo.count("v")
e_occurs = name_combo.count("e")
Love_occurs = l_occurs + o_occurs + v_occurs + e_occurs
print(Love_occurs)

LoveScore = int(str(True_occurs) + str(Love_occurs))
print(LoveScore)

if LoveScore < 10 or LoveScore > 90:
    print(f"Your score is {LoveScore}, you go like coke and mentos.")
elif LoveScore >= 40 and LoveScore <= 50:
    print(f"Your score is {LoveScore}, you are alright together.")
else:
    print(f"Your score is {LoveScore}")


