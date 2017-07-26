#!/usr/bin/python
# encoding:utf8
# Author:Along
_name = "along"
_passwd = "abc123"
name = input("name:")
passwd = input("password:")

if _name == name and _passwd == passwd:
    print("Welcome {name} loggin...".format(name=name))
else:
    print("invaild name or password")

