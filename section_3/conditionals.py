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

# short hand
