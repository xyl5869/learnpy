#!/usr/bin/python
# encoding:utf8
# Author:Along

oldboy_age = 56
count = 0

while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == oldboy_age:
        print("yes, you got it")
        break
    elif guess_age > oldboy_age:
        print("think smaller...")
    else:
        print("think bigger...")
    count += 1
else:
    print("you hava tried too many times...fuck off!")
