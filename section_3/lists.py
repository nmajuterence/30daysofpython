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

# exercise