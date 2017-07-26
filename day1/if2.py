#!/usr/bin/python
# encoding:utf8
# Author:Along

number = 23
guess = int(input('Enter a integer:'))

if guess == number:
    print('Yes,you guessed it.')
elif guess < number:
    print('No,think bigger.')
else:
    print('No,think lower.')
print('Done')