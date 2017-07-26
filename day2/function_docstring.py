#!/usr/bin/python
# encoding:utf8
# Author:Along
def print_max(x,y):
    '''Print the maximum of two numbers.

The two values must be integers.'''

    x = int(x)
    y = int(y)

    if x > y:
        print(x,'is the maximum')
    elif x == y:
        print(x,'is equal to',y)
    else:
        print(y,'is the maximum')

print_max(3,5)
print(print_max.__doc__)