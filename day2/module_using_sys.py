#!/usr/bin/python
# encoding:utf8
# Author:Along
import  sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n''The PYTHONPATH is', sys.path,'\n')