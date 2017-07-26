#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:Along

list_1 = [1,4,5,7,3,6,7,9,4]
list_1 = set(list_1)

list_2 = set([2,6,0,66,22,8,4])
print(list_1,list_2)

#交集
print(list_1.intersection(list_2))
print(list_1 & list_2)  #运算符格式

#并集
print(list_1.union(list_2))
print(list_1 | list_2)  #运算符格式

#差集
print(list_1.difference(list_2))    #in list_1 but not in list_2
print(list_1 - list_2)  #运算符格式in list_1 but not in list_2
print(list_2.difference(list_1))    #in list_2 but not in list_1
print(list_2 - list_1)  #运算符格式in list_2 but not in list_1

#子集
list_3 = set([1,3,7])
print(list_3.issubset(list_1))  #子集
print(list_3 <= list_1) #运算符格式

print(list_1.issuperset(list_3))    #父集
print(list_1 >= list_3) #运算符格式

#对称差集
print(list_1.symmetric_difference(list_2))  #返回list_1与list_2中不重复的的元素
print(list_1 ^ list_2)  #运算符格式

#判断两个集合是否没有交集
list_4 = set([2,4,6,8])
print(list_3.isdisjoint(list_4))

#添加一项元素
list_1.add(999)
print(list_1)

#添加多项元素
list_1.update([777,888,666])
print(list_1)

#删除一项元素,如果元素不存在则会报错
list_1.remove(888)
print(list_1)

#删除并返回一个任意的集合元素。 如果集合是空的，就会增加关键错误。
print(list_1.pop())
print(list_1)
print(list_1.pop())
print(list_1)

#如果是成员，就从集合中删除一个元素。 如果元素不是成员，则什么都不做。
print(list_1.discard("777"))

#判断x是否在集合成员
print(1 in list_1)

#判断x是否非集合成员
print(2 not in list_1)

#复制
list_5 = list_1.copy()
print(list_5)
