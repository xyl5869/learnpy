#!/usr/bin/python
# encoding:utf8
# Author:Along
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in the new zoo is', new_zoo)
print('Animal brought from old zoo is', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Nunber of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2]))