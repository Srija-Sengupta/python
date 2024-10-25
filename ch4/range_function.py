for value in range(1, 5):   # Will print only till 4 (off by one behavior)
    print(value)

# Making lists using range
numbers = list(range(1,6))
print(f'\n{numbers}')
# OR
number = []
for value in range(1,6):
    number.append(value)
print(numbers)

# Skip a number
even_num = list(range(0,11,2))  # 3rd argumenent acts as a step size
print(even_num)

square = []
for value in range(1,6):
    square.append(value**2)
print(square)

# Simple statistics
digits = [1,2,3,4,5]
print(f'\nThe smallest number is : {min(digits)}')
print(f'The largest number is : {max(digits)}')
print(f'The sum of all the numbers in the list is : {sum(digits)}')
