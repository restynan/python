# List comprehesion cuts down  on the amount of coding
# e.g

'''
new_list = []
for num in numbers:
    new_list.append(num+1)
print(new_list)
'''
numbers = [1, 2, 3, 4]
print(f'numbers : {numbers}')

increased_by_one = [num + 1 for num in numbers]
print(f'increased_by_one : {increased_by_one}')

doubled_numbers_in_range = [num * 2 for num in range(10, 15)]
print(f'doubled_numbers_in_range: {doubled_numbers_in_range}')

# conditional list compression
# get names that are made up of 4 letters or less
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(f'short_names: {short_names}')

# convert names  with length 5 and greater to have uppercase
long_names = [name.upper() for name in names if len(name) >= 5]
print(f'long_names: {long_names}')

# print squared numbers
squared_numbers = [num**2 for num in numbers]
print(f'squared_numbers: {squared_numbers}')

# print even numbers
even_numbers = [num for num in numbers if num % 2 == 0]
print(f'even_numbers: {even_numbers}')