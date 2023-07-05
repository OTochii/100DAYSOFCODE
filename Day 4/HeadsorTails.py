import random
'''
Module Test.
import my_module
radius = 2.5
circumference = 2.0 * my_module.pi * radius
result = "{:.2f}".format(circumference)
print(result)

Random Integer.
random_integer = random.randint(1, 5)
#print(random_integer)

#Random Float.

random_float = random.random()
#print(random_float)

random_decimal = random_float * 5
print(random_decimal)
'''

coin_toss = random.randint(0, 1)

if coin_toss == 1:
    print("Heads")
else:
    print("Tails")