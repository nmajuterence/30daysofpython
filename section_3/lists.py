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
print('centre' in regions_in_cameroon)
print('south west' in regions_in_cameroon)

# add items in a list
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
shoping_list.remove('groundnut')
print(shoping_list)

# removing items using del()
fruits = ['apple', 'bannana', 'pear', 'carrots', 'watermelon']
del fruits[0]
print(fruits)