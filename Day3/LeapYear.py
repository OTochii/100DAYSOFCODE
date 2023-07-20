Year = int(input("Which year do you want to check? "))

"""On every year that is evenly divided by 4
        except every year that is evenly divisible by 100
            unless the year is also evenly divisible by 400"""

if Year % 4 == 0 and Year % 100 == 0 and Year % 400 == 0:
    print("Year is a leap year.")
else:
    print("Year is not a leap year.")
    
     
     
     
    # and Year % 100 == 0 and Year % 400 = 0):
    
    
    #("Year is a leap year.")