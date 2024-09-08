# Method 1: Organizing Alphabetically (Permanent)
# Cannot revert back to original order
city = ['delhi','mumbai','kolkata','chennai']
city.sort()
print(city)

city.sort(reverse=True)     # Sorts in reverse alphabetical order
print(city)

# Method 2: By making a sorted copy of the list
# Doesnot affect the original list
city = ['delhi','mumbai','kolkata','chennai']
sorted_city = sorted(city)
print(f"\nHere's the sorted list : {sorted_city}")
sorted_city = sorted(city, reverse=True)
print(f"Here's the reversed sorted list : {sorted_city}")
print(f"Here's the original list : {city}\n")

# Printing a list in reverse order
# changes permanently
city = ['delhi','mumbai','kolkata','chennai']
city.reverse
print(city)

# length of a list
print(f'\nI have been to {len(city)} places')