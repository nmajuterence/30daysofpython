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

for i in range(0, 101, 10):
    print(i)
    
countries_new = ['cameroon', 'nigeria', 'ghana', 'south africa', 'rwanda', 'kenya', 'niger']
countries_with_ni = []
countries_without_ni = []

# countries with 'ni'
for i in countries_new:
    if 'ni' in i:
        countries_with_ni.append(i) # create new list with countries having 'ni'
print(countries_with_ni)

# countries without ni
for i in countries_new:
    if 'ni' not in i:
        countries_without_ni.append(i)
print(countries_without_ni)

# filter even numbers from 1 to 100
evens = []
for i in range(101):
    if i % 2 == 0:
        evens.append(i)
print(evens)

# filter odd numbers from 1 to 100
odds = []
for i in range(101):
    if i % 2 is not 0:
        odds.append(i)
print(odds)

# square numbers
for i in range(1, 11):
    print('{} * {} = {}'.format(i, i, i * i)) 

"""# using contine
nums1 = [0, 1, 2, 3, -7, 4, 5, 6]
for i in nums1:
    if i < 0:
        continue # continue skips the literal which matches the condition.
    print(i)

# using break
for i in nums1:
    if i < 0:
        break # break stops the loop when the condition is fufilled.
    print(i)"""

# excercises
# level 1
# 1. Iterate 0 to 10 using for loop, do the same using while loop.
# for loop
num_1 = []
for i in range(10):
    num_1.append(i)
print(f'iterate from 0 to 10: {num_1}')

# while loop
num_2 = []
i = 0
while i < 10:
    num_2.append(i)
    i = i + 1
print(num_2)

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
# for loop
num_1a = []
for i in range(9, -1, -1):
    num_1a.append(i)
print(num_1a)

# while loop
num_2a = []
i = 0
while i > -10:
    i = i - 1
    num_2a.append(i)
print(num_2a)

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
i = 1
while i <= 7:
    print('#' * i)
    i += 1