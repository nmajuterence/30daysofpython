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

