#!/usr/bin/python
# encoding:utf8
# Author:Along

oldboy_age = 56
guess_age = int(input("guess age:"))

if guess_age == oldboy_age:
    print("yes,you got it!")
elif guess_age > oldboy_age:
    print("think smaller...")
else:
    print("think bigger...")

