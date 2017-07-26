#!/usr/bin/python
# encoding:utf8
# Author:Along
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist

#我购买了第一项项目，所将其从列表中删除
del shoplist[0]
print('shoplist is',shoplist)
print('mylist is',mylist)

print('Copy by making a full slice')
mylist = shoplist[:]
del mylist[0]
print('shoplist is',shoplist)
print('mylist is',mylist)