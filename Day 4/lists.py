import random
'''
# Split String

names_string = input("Give me everybody's names, seperated by a comma. ")
names =  names_string.split(", ")

# Find the length of list

list_length = len(names)
print(list_length)

# Create a random generator to shuffle names

list_shuffle = random.randint(0, list_length - 1)
print(list_shuffle)
print(f"{names[list_shuffle]} is paying the bill")


Alternatively, using random.choice() to pick a random name from list...

OneWhoPays = random.choice(names)
print(f"{OneWhoPays} is going to buy the meal today.")
'''
# Append and initialize a list by index
fruits = ["Apples", "Cherries", "Orange", "Grapes", "Peaches", "Pears"]
#fruits[-1] = "Melons"
fruits.append("Lemons")
#print(fruits)

# Nested List
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potato"]
dirty_dozen = [fruits, vegetables]

# Print the element at index 1 in the first list
print(dirty_dozen[0][1])