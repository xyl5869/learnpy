#!/usr/bin/python
# encoding:utf8
# Author:Along
name = 'my \tname is {name} and I am {year} old'
name1 = {'name':'along','year':24}
address = 'xieyl@darenloan.com'
print(name.capitalize())    #将字符串设定为首字母大写
print(name.count("a"))      #统计指定字符在字符串中出现的次数
print(name.center(80,"-"))      #指定字符串居中，左右两边用指定的字符填充（默认为空格）
print(address.endswith(".com"))     #判断字符串是否以指定的字符为结尾，常用
print(name.expandtabs(tabsize=1))      #将字符创的tab符(\t)转为空格，默认空格数为8
print(name.find("name"))    #查找字符是否在字符串中，如果在则返回其索引值,否则返回-1
print(name.format(name='along',year=23))    #格式化输出
print(name.format_map(name1))   #格式化输出，以字典中的值
print('fdafd212'.isalnum())     #判断字符串是否为字母+数字
print('fds  fdsa'.isidentifier())       #判断字符串是否符合变量命名规则
print('abc'.islower())      #判断字符串是否全部为小写
print('1234'.isnumeric())       #判断字符串是否为数字
print(' '.isspace())        #判断字符串是否为空格
print('My Name Is Along'.istitle())     #判断字符串是否符合标题化，每个单词首字母大写
print('jkladf'.isprintable())#tty file,drive file...    #判断字符串是否可打印，只在文件类型为tty或drive有效
print('ABC'.isupper())      #判断字符串是否全部为大写
'''
print('+'.join(['1','2','3','4']))
print(name.ljust(50,'*'))   #将字符串左对齐，并且使用填充符（默认为空格）填充至指定的长度
print(name.rjust(50,'-'))   #将字符串右对齐，并且使用填充符（默认为空格）填充至指定的长度
print('Along'.lower())  #将字符串改为小写
print('Along'.upper())  #将字符串改为大写
print('   \nAlong'.lstrip())    #去除字符串左边的空格和换行符
print('Along\n   '.rstrip())    #去除字符串右边的空格的换行符
print('   \nAlong\n'.strip())   #去除字符串左右两边的换行符，常用
print('--------')

p = str.maketrans("abcdef","123456")    #将两个字符串按顺序一一对应
print('alex li'.translate(p))   #转换字符串为上面对应的顺序

print('alex li'.replace('l','L',1))     #替换字符串中的某一段字符串

print('alex lil'.rfind('l'))    #找出最右匹配到字母的下标
print('al ex lil'.split('l'))      #按指定的字符串作为分隔符，默认为空格

print('Alex li'.swapcase())     #将小写装为大写，将大写装为小写

print('alex li'.title())    #首字母大写

print('alex li'.zfill(10))  #指定字符串长度，不够的前面补零
'''