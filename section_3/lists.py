# list
shoping_list = ['milk', 'meat', 'rice', 'beans', 'fish']
print(shoping_list)
print(len(shoping_list))
numbers = [1, 2, 3, 4, 5, 6]
regions_in_cameroon = ['north west', 'south west', 'litoral', 'centre', 'east', 'north']
names = ['frida', 'kiara', 'nmaju', 'maureen', 'thelly']
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
print(numbers[5])

# get the last index of a list
last_index = len(numbers) - 1
print(last_index)

# string slicing numbers[start:end:step]
print(numbers[2:])
print(numbers[1:5])
print(numbers[::-1]) # reverses the list
print(numbers[:3])
print(numbers[-3:-1])

# modifying a list
numbers[-1] = 50
print(numbers)
numbers[2] = 33
print(numbers)

# remove items from a list pop() removes the last item of the list
numbers.pop()
print(numbers)
numbers.pop(1) # the item at index 1 will be removed
print(numbers)

# inserting an item into a list
numbers.insert(1, 22)
print(numbers)
numbers.insert(2, 400)
print(numbers)

# checking items in a list
print(regions_in_cameroon)
print('centre' in regions_in_cameroon) # true
print('south west' in regions_in_cameroon) #true
print('douala' in regions_in_cameroon) # false

# add items in a list apend() adds an item to the end of the list.
shoping_list = []
print(shoping_list)
shoping_list.append('milk')
shoping_list.append('meat')
shoping_list.append('vegetables')
shoping_list.append('groundnut')
shoping_list.append('beans')
shoping_list.append('garri')
print(shoping_list)

# remove items from a list
print(shoping_list)
shoping_list.remove('groundnut') # remove searches for an item and deletes it without using the index
print(shoping_list)

# removing items using del()
fruits = ['apple', 'bannana', 'pear', 'carrots', 'watermelon']
del fruits[0] # del deletes an item from a particular index
print(fruits)

# clearing the list clear()
fruits.clear() # it empties the list it also means empty the list
fruits = []
fruits = list() # same as fruits = []
print(fruits)

# joining list
positive_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
negative_numbers = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
zero = [0]
print(negative_numbers[::-1] + zero + positive_numbers) # [::-1] reverses the order of the list

# counting items in a list
fruits_new = ['apples', 'bannana', 'pawpaw', 'mango', 'oranges']
print(fruits_new.count('apples')) # count() takes an item as an argument
ages_new = [22, 19, 24, 25, 30, 26, 24, 25, 24]
print(ages_new.count(24))

# finding the index of an item
ages_new = [22, 19, 24, 25, 30, 26, 24, 25, 24]
print(ages_new.count(25))
print(ages_new.index(25)) # checks the index of 25

# reversing a string reverse
print(ages_new)
ages_new.reverse()
print(ages_new) # reverse() mutates the data: the original data is no longer the same

# sorting a list
ages_new = [22, 19, 24, 25, 30, 26, 24, 25, 24]
sorted_age = sorted(ages_new) # sorted() does not mutate the data
print('using sorted: ',sorted_age)
ages1 = [22, 19, 24, 25, 30, 26, 24, 25, 24]
ages1.sort()
print('using sort: ',ages1) # sort() also mutates the data

# exercises: level 1
new_list = list()
new_list1 = ['nmaju', 'kiara', 'frida', 'maureen', 'enih', 'noella']
print('length of new list 1: ',len(new_list1))
print('first item: ',new_list1[0]) # first item
print('middle item: ',new_list1[3]) # middle item
print('last item: ',new_list1[5]) # last item
mixed_data_types = ['nmaju', 30, 1.75, 'married', 'antenne orange']
companies = ['facebook', 'google', 'microsoft', 'apple', 'ibm', 'oracle', 'amazon']
print('companies: ',companies)
print('number of companies: ', len(companies)) # 7 companies
print('the first company is ',companies[0]) # facebook is the first company
print('the middle company is ',companies[3]) # apple is the middle company
print('the last company is ',companies[-1]) # amazon is the last company
companies[0] = 'meta' # facebook is now meta
print(companies)
companies.append('IT company')
print(companies)
companies.insert(3,'IT company')
del companies[-1] # deletes IT company at the last index
print(companies)
print(companies.index('ibm'))
companies[5] = companies[5].upper()
print(companies)
# print('#; '.join(companies))
print('bygtee' in companies)
lst = ['facebook', 'google', 'microsoft', 'apple', 'ibm', 'oracle', 'amazon']
lst.sort() # asending order
lst.sort(reverse=True) # descending order
print(lst)
"""print(lst[:3]) # slicing the first 3 companies
print(lst[-3:]) # slicing the last 3 companies
print(lst[3:4]) # slicing the middle company"""
lst.pop(0)
print(lst)
lst.pop(3)
print(lst)
lst.pop()
print(lst)
lst.clear()
print(lst)
del lst # it deletes the list completely
front_end = ['html', 'css', 'js', 'react', 'redux']
back_end = ['node', 'express', 'mongodb']
full_stack = front_end + back_end
print(full_stack)
full_stack.insert(9, 'python')
full_stack.insert(10, 'sql')
print(full_stack)