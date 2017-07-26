#!/usr/bin/python
# encoding:utf8
# Author:Along
def func(a,b=5,c=10):
    print('a is',a, 'and b is',b, 'and c is',c)

func(3,6)
func(65,c=64)
func(c=50,a=20)