import random
'''
Rules
1. Rock wins against scissors
2. Scissors wins against paper
3. Paper wins against rock
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user  = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
if user == '0':
       user0 = rock
       print(f"You chose: {user0}")
elif user == '1':
       user1 = paper
       print(f"You chose: {user1}")
else:
       user2 = scissors
       print(f"You chose: {user2}")

computer = random.randint(0, 2)
if computer == 0:
       computer0 = rock
       print(f"Computer chose: {computer0}")
elif computer == 1:
       computer1 = paper
       print(f"Computer chose: {computer1}")
else:
       computer2 = scissors
       print(f"Computer chose: {computer2}")
       
if int(user) == computer:
       print("It's a draw")
elif int(user) == 2 and computer == 1:        
        print("You win")
elif int(user) == 1 and computer == 0:        
        print("You win")
elif int(user) == 0 and computer == 2:
    print("You win")
else:
       print("You lose")    