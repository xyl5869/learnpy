#!/usr/bin/python
# encoding:utf8
# Author:Along
#names = "Zhangyang Guyun Xiangpeng XuLiangChen"

names = ["Zhangyang","Guyun","Xiangpeng","XuLiangChen"]
print(names)
names.append("LeiHaidong") #列表追加成员到最后
names.insert(1,"ChenRongHua") #插入成员到列表中，1为要插入的位置
names.insert(3,"Xinzhiyu") #插入成员到列表中，3为要插入的位置
print(names)
names[2] = "XieDi"
print(names)

#delete
#names.remove("ChenRongHua") #用remove方法直接删除成员
#del names[1] #用del删除列表中指定的下标
#names.pop(1) #用pop方法剔除列表中指定的下标，如果未指定下标默认剔除最后一个成员
#print(names)

#index
print(names.index("XieDi")) #使用列表的index方法，查询成员所在列表中的成员下标位置，只返回找到的第一个下标
print(names[names.index("XieDi")]) #去成员的下标位置后，再用列表取该下标并打印出来

names.reverse() #翻转列表中成员的位置。
#names.clear() #清空列表
names.sort() #对列表中的成员按ASCII编码进行排序
print(names)

names2 = [1,2,3,4]
names.extend(names2) #使用列表的方法extend，对列表进行扩展，将连个列表合并
print(names)

print(names.count('XieDi')) #使用.count方法对列表中的成员进行统计出现的次数
#print(names[0],names[2])
#print(names[1:3]) #切片
#print(names[3]) #
#print(names[-1]) #取最后一个，在不知道列表有多长的情况下非常好用
#print(names[-2:]) #取最后两个，注意切片的顺序是自左往右数的，这里要留空，而不是填-1，否则只能取倒数第二个
#print(names[:3]) #取前三个，所以0也可以忽略