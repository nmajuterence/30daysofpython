# strings and string methods
letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'
consonants = 'bcdfgjklmnpqrstvwxyz'

# strings: len()
print('letters of the alphabet:', letters)
print('number of letters:', len(letters))
print('vowels:', vowels)
print('number of vowels:', len(vowels))
print('consonants:', consonants)
print('number of consonants:', len(consonants))

# strings: uppe(), lower(), swapcase(), title()
last_name = 'nmaju'
print(last_name)
print('Upper case:', last_name.upper())
print('Lower case:', last_name.lower())
title_case = last_name.title()
print('Swap case:', title_case.swapcase())

# index: every character of a string in stored in an index [0,1,2,3,4,5]
challenge = '30 days of python with nmaju'
print(challenge.find('j')) # the method find() check the index where 'j' is being stored
print(challenge.find('o')) # with duplicate characters, the find() shows only the first instance of the character

# string slicing
language = 'python'
print(len(language)) # there are 6 characters so it starts from index 0 to index 5
print(language[0:2]) # prints only chracters from index 0 to index 2 (excluding index 2)
print(language[2:]) # prints from index 2 to the last index
print(language[-2:]) # prints from 'o' 
print(language[::-1]) # prints the variable content in reverse
print(language.count('o')) # prints the number of times 'o' appears in language

city = 'bamenda'
print(city.count('a')) # count the number of a's in the string
print(city.find('a')) # finds the first occourance of 'a'

print('i love python'.capitalize()) # capitalize() capitalizes only the first letter of the string
print('i love python'.title()) # title() capitalizes the first letter of each word

country = 'cameroon'
print(country.startswith('ca')) # startswith() checks the string for 'ca'
print(country.endswith('oon')) # true
print(country.startswith('C')) # false

skills = ['html', 'css', 'javascript', 'python']
print(', '.join(skills)) # join() uses the string you provide to join the elements of the list

print('abc'.isalpha()) # true
print('abc123'.isalnum()) # true
print('123'.isnumeric()) # true
print('0x1b3'.isascii()) # true

# isidentifier() simples test if the string can be a variable name
# first_name, last_name, year etc
print('first_name'.isidentifier()) # true
print('2024year'.isidentifier()) # false because 2024year is not a valid variable name

# replace() this method can replace a string with another string
slogan = 'welcome to the 2024 JavaScript bootcam with nmaju in cameroon.'
print(slogan.replace('JavaScript', 'python')) # here JavaScript is replaced with python
print(slogan.replace('javascript', 'python')) # note that python is case sensitive so this line of code will not work

# exercise
# recap

first_name = 'terence'
last_name = 'nmaju'
age = 30
city = 'douala'
country = 'cameroon'
skills = ['html', 'css', 'javascript', 'python']
full_name = first_name + ' ' + last_name
skill_set = ', '.join(skills)
print(full_name)

# reprint the text below using the variables
# i am terence nmaju. i am 30 years old. i live in douala, cameroon. i have skills in html, css, javascript, python.

# method 1 - string concatination
profile_1 = 'i am ' + full_name + '. ' + 'i am ' + str(age) + ' years old. i live in ' + city + ', ' + country + '. i have skills in ' + skill_set + '.'
print('profile 1: ', profile_1)

# method 2 - .format()

profile_2 = 'i am {}. i am {} years old. i live in {}, {}. i have skills in {}.'.format(full_name, age, city, country, skill_set)
print('profile 2: ', profile_2)

# method 3 - f string

profile_3 = f'i am {full_name}. i am {age} years old. i live in {city}, {country}. i have skills in {skill_set}.'
print('profile 3: ', profile_3)

# example
a = 4
b = 3

# method 1
print('%d + %d = %d' %(a, b, a + b))
print('%d - %d = %d' %(a, b, a - b))
print('%d * %d = %d' %(a, b, a * b))
print('%d / %d = %.2f' %(a, b, a / b))
print('%d %% %d = %d' %(a, b, a % b)) 
print('%d ** %d = %d' %(a, b, a ** b))

# method 2 
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b)) 
print('{} ** {} = {}'.format(a, b, a ** b))

# method 3
div = a / b
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {div:0.2f}') # 0.2f set the float to 2 decimal places
print(f'{a} % {b} = {a % b}') 
print(f'{a} ** {b} = {a ** b}')

sentence = 'i love python'
print(sentence.split()) # split() it can split the sentence into a list of words
print(sentence.split(' love ')) # here it removes love from the list.
print('i love python \nvery much') # \n starts the text on a new line.
print('i don\'t like this') # \ is an escape character
print('the old cliche of \'an apple a day keep the doctor away\' might not work') # another example
print('firstname','\t', 'lastname', '\t','age', '\t','city', '\t' 'country')
print('terence','\t', 'nmaju', '\t','30', '\t','douala', '\t' 'cameroon')

# assignment
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string = ['thirty', 'days', 'of', 'python']
print(' '.join(string))

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string_2 = ['coding', 'for', 'all']
new_string = ' '.join(string_2)
print(new_string)
print(len(new_string))
print(new_string.upper())
print(new_string.lower())
print(len(new_string))
print(new_string.capitalize())
sentence_case = new_string.title()
print(sentence_case.swapcase())
print(new_string[7:])
print(new_string.find('coding'))
uncut_str = ' '.join(string_2)
print(uncut_str.replace('coding', 'python'))
print(uncut_str.split(' '))

# testing split()
test_string = 'nmaju,is,a,python,programmer'
print(test_string.split(',', 4)) # 4 is the number of splits

test_string2 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(test_string2.split(',')) # using ',' as a seperator

# print the character at index 10
string_3 = 'Coding For All'
character_at_index_10 = string_3[10]
print(character_at_index_10)

# print the last index of the string
last_str_index = string_3[-1] # -1 is the last index
print(last_str_index)

# create an acronym of the name 'Python For Everyone'
name = 'Python For Everyone'
abb_P = name[0]
abb_F = name[7]
abb_E = name[11]
acronym = [abb_P, abb_F, abb_E]
print('.'.join(acronym))

# use index to determine the position of the first occurrence of C
main_string = 'Coding For All'
char = 'C'
position = main_string.index(char)
print(position)

# use rfind to determine the position of the last occurrence of l
test_str = 'Coding For All People'
char = 'l'
position_l = test_str.rfind(char)
print(position_l)

#Use index or find to find the position of the first occurrence of the word 'because'
bcuz = 'You cannot end a sentence with because because because is a conjunction'
print(bcuz.find('because'))