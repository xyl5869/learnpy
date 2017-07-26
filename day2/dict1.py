#!/usr/bin/python
# encoding:utf8
# Author:Along

info = {
    'stu1101':"TengLan Wu",
    'stu1102':"LongZe Luola",
    'stu1103':"XiaoZe Maliya"
}
'''
print(info)
# print(info['stu1101'])    #按key来查找其值，如果key不存在则会报错
print(info.get('stu1104'))  #推荐使用个，安全的查找键值方法，key存在则获取其值，key不存在则返回None

print('stu1103' in info)    #判断字典中是否有该key，python2.x中使用info.has_key("stu1103")
info['stu1101'] = "Wu TengLan" #如果键值存在则修改其值，如果不存在则添加一对键值
print(info['stu1101'])
info['stu1104'] = "Cang Jinkong"    #键值不存在则添加一对键值
print(info)

#删除
#del info['stu1101']    #python自带删除方法
info.pop('stu1101')     #标准删除方法
info.popitem()      #随机删除方法
print(info)
'''

#print(info.clear())     #删除字典
#print(info.values())    #只查询字典里的值
#print(info.keys())      #只打印字典中的key

#print(info.items())     #打印字典里的键值对，并以列表中的元组方式输出

#print(info.setdefault('stu1101',None))   #查找字典，如果存在该键值就打印出来，如果不存在就插入改键值对
#print(info.setdefault('stu1104','Cangjinkong'))
#print(info)

'''
info1 = {"stu1104":'Cangjinkong'}
info.update(info1)  #添加一个字典到另外一个字典
print(info)
'''
#字典的循环
#for i in info:
#    print(i,info[i])

'''
#多级字典嵌套及操作
catalog = {
    "中国":{
        "www.baidu.com":["中国第一大搜索引擎","垄断地位"],
        "www.sougo.com":["搜狐旗下搜索引擎","搜索结果不理想"]
    },
    "欧美":{
        "www.google.com":["世界第一大搜索引擎","搜索效率高"],
        "www.bing.com":["微软旗下搜索引擎","国内大多用来代替百度"]
    },
    "日韩":{
        "www.yahoo.co.jp":["日本常用的搜索引擎","雅虎的日本站点"]
    }
}

catalog["中国"]["www.baidu.com"][1] += ",尽量少使用"
print(catalog["中国"]["www.baidu.com"])
'''