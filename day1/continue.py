#!/usr/bin/python
# encoding:utf8
# Author:Along
while True:
    s = input('Enter something:')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')