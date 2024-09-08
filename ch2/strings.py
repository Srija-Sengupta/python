#methods
str="hi srija here"
print(str.title()) #makes letter of each word in cap
print(str.upper()) #makes the entire string in caps
print(str.lower())#makes the entire string in lowercase
# f strings
f_name = 'Srija'
l_name = 'Sengupta'
name = f'{f_name} {l_name}'
print(f"\nWelcome {name.title()}")

# Adding Whitespaces
str = "Srija"
str2 = "Sengupta"
print(f"\t{str}\n{str2}")

# stripping whitespaces(temporarily)
city = 'kolkata '
print(city.rstrip())    # right strip
print(city.lstrip())    # left strip
print(city.strip())     # strip both sides

# stripping whitespaces(permanently)
city = city.strip()
print(city)

# removing prefixes
str = "kolkata is a beautiful city "
str2 = str.removeprefix('kolkata')
print(str)
print(f'Mumbai{str2}')