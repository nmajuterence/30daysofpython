# conditionals
# if and else statements
a = 0.5
if type(a) == int:
    if a > 0:
        print('{} is a positive number'.format(a))
    elif a < 0:
        print('{} is a negative number'.format(a))
    elif a == 0:
        print('{} is zero'.format(a))
    else:
        print('{} is not a number'.format(a))
else:
    print('{} is a float'.format(a))

"""# exercise level 1 a
age = int(input('Enter your age: '))
if age >= 18:
    print('you are old enough to learn to drive')
else:
    print(f'you need {18 - age} more years to drive') # the expression {18 - age} calculates the number of year rmaining to drive.

# exercise level 1 b
your_age = int(input('Enter your age: '))
my_age = 25
if your_age > my_age:
    print('you are {} years older than me'.format(your_age - my_age))
elif your_age == my_age:
    print('we are both the {} years old.'.format(your_age))
else:
    print('you are {} years younger than me'.format(my_age - your_age))

# exercise level 1 c
a = int(input('enter the value of a: '))
b = int(input('enter the value of b: '))
if a > b:
    print(f'{a} is greater than {b}.')
elif a < b:
    print(f'{a} is smaller than {b}.')
else:
    print(f'{a} is equal to {b}.')

# exercise level 2 a
score = int(input('enter your score: '))
if score >= 80 and score <= 100:
    print('your grade is an "A"')
elif score >= 70 and score < 80:
    print('your grade is a "B"')
elif score >= 60 and score < 70:
    print('your grade is a "C"')
elif score >= 50 and score < 60:
    print('your grade is a "D"')
else:
    print('your grade is an "F"')

# exercise level 2 b
month = input('enter a month to check the season: ')
if month == 'september' or 'october' or 'november':
    print('the season is autumn')
elif month == 'december' or 'january' or 'february':
    print('the season is winter')
elif month == 'march' or 'april' or 'may':
    print('the season is spring')
elif month == 'june' or 'july' or 'august':
    print('the season is summer')
else:
    print('please enter a real month or check your spelling!')"""
    
# exercise level 3a
person={
    'first_name': 'nmaju',
    'last_name': 'terence',
    'age': 30,
    'country': 'cameroon',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'antenne orange',
        'city': 'douala',
        'zipcode': '237'
    }
}
if person['skills']:
    print(person['skills'][2])
else:
    print('the skills list is empty')

# exercise level 3b
if person['skills']:
    if person['skills'][4] == 'Python':
        print(person['skills'][4])
    else:
        print('Python is not one of the skills')
else:
    print('python is not in the dictionary')

# exercise level 3c
if 'JavaScript' in person['skills'] and 'React' in person['skills'] and len(person['skills']) == 2:
    print('he is a front end developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
   print('he is a back end developer')
elif 'Node' in person['skills'] and 'React' in person['skills'] and 'MongoDB' in person['skills']:
    print('he is a fullstack developer')
else:
    print('unknown title')