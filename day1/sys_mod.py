#!/usr/bin/python
# encoding:utf8
# Author:Along
'''import sys
#print(sys.path) #打印环境变量
print(sys.argv[3])'''

'''import os
#os.system("dir")
cmd_res = os.popen("dir").read()
print(cmd_res)'''

print('我爱北京天安门'.encode('gb18030'))
print('我爱北京天安门'.encode('gb18030').decode('gb18030'))

msg = "我爱北京天安门"
bmsg = msg.encode("utf-8")
print(bmsg)
smsg = bmsg.decode("utf-8")
print(smsg)