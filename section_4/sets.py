# sets in python
print(set()) # printing an empty set
print(len(set()))
a = {1, 2, 3, 4, 5, 6, 9} # here is how a set is written
b = {3, 4, 5 , 8, 9}

# membership
print(7 in a) # false
print(4 in a) # true

# access items in a set
for item in a:
    print(item)

# add items
a.add(10)
print(a)

# add many items. you can add many items via a list or tuple
a.update([13, 17, 11, 67]) # adding items using a list
print(a)
a.update((20, 21, 39))
print(a)

# remove items
a.remove(10)
print(a)
a.pop() # removes on random item
print(a)

# operations of sets or set methods
inter = a.intersection(b)
print('a intersection b = {}'.format(inter))
union = a.union(b)
print('a union b = {}'.format(union))
diff = a.difference(b)
print('a without b = {}'.format(diff))
symdiff = a.symmetric_difference(b)
print('symetric difference of a and b = '.format(symdiff))

# converting a list to a set

fruits = ['bannan', 'orange', 'mango', 'orange', 'lemon', 'apple']
print(set(fruits)) # sets don't accept duplicate items. here is how to convert a list to a set
