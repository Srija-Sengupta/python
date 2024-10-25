# Checking if a list is empty or not

requested_drinks = []

if requested_drinks:
    for requested_drink in requested_drinks:
        print(f"Adding {requested_drink} to your meal")
    print("Your meal is ready :) ")
else:
    print("Are you sure you wanna have just a burger? :( ")
print("\n")


# Using Multiple lists
available_beverages = ['masala chai', 'cold coffee','frappe','latte','mocha','americano']
requested_beverages = ['latte','mocha','frappe','cappucino']

for requested_beverage in requested_beverages:
    if requested_beverage in available_beverages:
        print(f"Adding {requested_beverage} to your meal :)")
    else:
        print(f"sorry we are out of {requested_beverage} :( ")