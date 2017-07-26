#!/usr/bin/python
# encoding:utf8
# Author:Along
data = {
    '北京':{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":["CICC","HP"],
            "东直门":["Advent","飞信"]
        },
        "海淀":{}
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    '广东':{
        "深圳":{},
        "广州":{},
        "佛山":{}
    }
}

exit_flag = False
while not exit_flag:
    for i in data:
        print(i)
    choice = input("选择进入1>>:")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t",i2)
            choice2 = input("选择进入2>>:")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print("\t\t",i3)
                    choice3 = input("选择进入3>>:")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t\t",i4)
                        choice4 = input("最后一层，按b返回>>:")
                        if choice4 == "b" or choice4 == "B":
                            pass
                        elif choice4 == "q" or choice4 == "Q":
                            exit_flag = True
                    if choice3 == "b" or choice3 == "B":
                        break
                    elif choice3 == "q" or choice3 == "Q":
                        exit_flag = True
            if choice2 == "b" or choice2 == "B":
                break
            elif choice2 == "q" or choice2 == "Q":
                exit_flag = True
    if choice == "q" or choice == "Q":
        exit_flag = True
