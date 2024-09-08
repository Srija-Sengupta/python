# Method 1: Using Del (you need index pos)
city = ['delhi','mumbai','kolkata','chennai']
del city[2]
print(city)

# Method 2: Using pop (removes elements from end)
# Lets you work with the element after removing it.
city = ['delhi','mumbai','kolkata','chennai']
popped_city = city.pop()
print(f'\n{city}')
print(f'I used to live in {popped_city.title()}\n')

first_city = city.pop(0)    # popping from any position
print(f'{first_city.title()} is the first city in the list\n')

# Method 3: Removing by value
# Lets you work with the element after removing it.
city = ['delhi','mumbai','kolkata','chennai']
removed_city = 'kolkata'
city.remove(removed_city)
print(city)
print(f'I live in {removed_city}')

city.remove('chennai')
print(city)