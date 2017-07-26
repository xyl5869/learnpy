#!/usr/bin/python
# encoding:utf8
# Author:Along
goods_list = [['1.','iPhone',5800],['2.','Mac Pro',12000],['3.','StarBuck Latte',31],['4.','Alex python','81'],['5.','Bike','800']]
salary = int(input('请输入你的工资:'))
while True:

    for i in goods_list:
        print(i)
    shopping_cart = input('请挑选你心仪的商品:')
