# Check whether a value is 'IN' the list 

topping = ['mushrooms','onions','pineapple']
requested_toppings = 'anchovies'
if requested_toppings in topping:
    print(f"Put {requested_toppings} on the pizza ")
else:
    print(f"Sorry we are out of {requested_toppings}")
print("\n")


# Check whether a value is 'NOT' the list

banned_users = ['James','Andrew','Carolina','David','Liam']
user = 'james'
if user.title() not in banned_users:
    print("You can post anything")
else:
    print("Sorry you can't post anything")
print("\n")


# if-elif-else chain

income = 6969
if income < 10000:
    print("Work hard lol")
elif  income <= 40000:
    print("Still middle class lol")
elif income < 90000:
    print("Dayumm boy")
else :
    print("Take a bow!")
print("\n")


# Testing Multiple conditions
# Use Multiple if statements when you want to check all condtions

requested_toppings2 = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings2:
    print("adding Mushrooms")
if 'pepperoni' in requested_toppings2:
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings2:
    print("adding extra cheese")
print("\nFinished making your pizza")