# loops: a loop is a repeatition or iteration of a statement
# for loop

# greeting 100 people
print('happy new year')

people = [] # let's assume the name of each person is a serial number from 0 to 101
for i in range(3):
    people.append(i)
    print(f'happy new year {i}')

"""from countries import countries # importing the list of countries from countries.py

list_countries_ending_in_ca = []
for country in countries:
    list_countries_ending_in_ca.append(country) # add countries in the empty list
    print(list_countries_ending_in_ca)

# filter countries
countries_with_ca = []
for c in countries:
    if 'den' in c:
        countries_with_ca.append(c)
        print(countries_with_ca)"""

# add all numbers in a list
nums = [0, 1, 2, 3, 4, 5]
for num in nums:
    total = 0
    total = total + num
    print(f'total + {nums[num]} = {total}')

# Can you provide an example of a for loop that iterates over a list of numbers and prints each number?
numbers = [1, 3, 5, 7, 9]
for i in numbers:
    print(i)
