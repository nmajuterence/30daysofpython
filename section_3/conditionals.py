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

# exercise level 1 a
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
