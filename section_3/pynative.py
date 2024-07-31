# Write a program to create a new string made of an input string’s first, middle, and last character.
str1 = 'james'
str2 = str1[0:5:2] # slice the string
print(str2)

# Exercise 2: Append new string in the middle of a given string
s1 = 'Ault'
s2 = 'Kelly'
mid_s = len(s1) // 2 # the mid point
start_s1 = s1[0:2]
end_s1 = s1[2:]
new_string = start_s1 + s2 + end_s1
print(new_string)

