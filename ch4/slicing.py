fruits = ['mango','orange','banana','apple','guava']
print(fruits[1:3])  # Prints from index 1 till 2

# Omiting first index, prints from begining
print(f'The first four fruits in the list are {fruits[:4]}')

# Omitting ending index, prints till the end
print(fruits[2:])   

# Negative index
print(fruits[-3:])  # prints the last 3 fruits

cities = ['dubai','mumbai','kolkata','chennai','bangalore','delhi','pune','alwar']
print(cities[0::2])