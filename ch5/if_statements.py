# Simple Conditional statements
cars = ['audi', 'bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(f"yes we have a {car.title()}")

    else:
        print(f"{car.title()}")
print("\n")

# 1. Checking equality
# convert to smallcase if you're not sure about the case
car = 'Audi'
need = 'audi'
if car.lower() == need.lower():
    print(f"Yes we have an {car.title()}")

# 2. Checking for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("\nHold the anchovies\n")

# Multiple conditions
# Using And statement
age = 17 
height = 5.6
if age >= 18 and height > 5:
    print("You can go for the ride!")

else:
    print("Sorry you can't go for the ride")

# using or
age = 17 
height = 5.6
if age >= 18 or height > 5:
    print("You can go for the ride!")

else:
    print("Sorry you can't go for the ride")