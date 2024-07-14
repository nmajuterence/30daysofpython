# logical operators: and, or, not
a = 6
b = 3
c = 1

# and
print('and 1: a > b and b > c =', a > b and b > c) # true
print('and 2: a < b and b > c =', a < b and b > c) # false

# or 
print('or 1: a > b or b < c =', a > b or b < c) # true
print('or 2: a < b or b < c =', a < b or b > c) # true

# not, negation, negate
print('not 1: not a > b or not b < c =', not a > b or not b < c) # True
print('not 2: a < b or not b > c =', a < b or not b > c) # false
print('not 3: not a > b and not b > c =', not a > b and not b > c) # false
print('not 4: not a < b and b > c =', not a < b and b > c) # true