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

# exercise 1
age = int(input('Enter your age: '))
if age >= 18:
    print('you are old enough to learn to drive')
else:
    print(f'you need {18 - age} more years to drive') # the expression {18 - age} calculates the number of year rmaining to drive.


