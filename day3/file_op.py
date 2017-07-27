#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:Along

#data = open("yesterday",encoding="utf8").read()
#print(data)

'''
#r模式，r=read，只读模式打开文件，不能进行写操作，默认模式
f = open("yesterday",'r',encoding='utf8')
data = f.read()
print(data)
'''

'''
#w模式，w=write，只写模式，而且会覆盖该文件的原来数据，不能读文件
f = open("yesterday2",'w',encoding="utf8")
f.write("我爱北京天安门，\n")
f.write("天安门上太阳升")
data = f.read()
print(data)
'''

'''
#a模式，a=append，将数据追加到文件末尾,不能读文件
f = open("yesterday2",'a',encoding="utf8")   #文件句柄，包含文件的文件名，字符集，大小，硬盘起始位置等，统一包装成一个内存对象

f.write("\n我爱北京天安门，\n")
f.write("天安门上太阳升，")
'''

f = open("yesterday2",'a',encoding="utf8")
'''
#print(f.readline())     #readline函数，从第一行开始，每次打印一行

#使用for循环打印多行
#for i in range(5):
#    print(f.readline())

#不打印指定的行，有缺点，读大文件时不能使用，否则会撑爆内存
for index,line in enumerate(f.readlines()):
    if index == 9:
        print("我是分割线".center(50,'-'))
        continue
    print(line.strip())
'''
'''
#高级写法，每次循环一行，并打印一行，下一次循环会把内存中的line值覆盖，然后再打印。不会撑爆内存，可以读大文件
count = 0
for line in f:
    if count == 9:
        print("我是分割线".center(50,'-'))
        count += 1
        continue
    print(line.strip())
    count += 1
f.close()
'''

'''
#tell()方法是打印当前位置，seek方法是回退到任意位置
print(f.tell())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.seek(0)
print(f.readline())
'''

'''
#文件常用操作
print(f.encoding)   #打印当前文件的字符编码

print(f.fileno())   #打印文件的文件描述符序号

print(f.name)   #打印文件名

print(f.seekable())     #判断文件是否可以跳转

print(f.readable())     #判断文件是否可读

print(f.writable())     #判断文件是否可写

print(f.flush())    #将文件在内存中的buffer写到磁盘中去

f.truncate(9)    #截断，参数可以指定要保留的字符，如果不指定从文件开头开始截断，文件的打开方法必须是a
'''