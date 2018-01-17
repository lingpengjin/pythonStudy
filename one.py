#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a = 2
b = a
a = 3
print(b)
c = "Hello World!"
print(c)
print('汉字')
print(ord('汉'))
print(ord('字'))
print(chr(27721), chr(23383))
print('\u4e2d\u6587')

d = '汉字'
print(d.encode('utf-8'))
print(b'\xe6\xb1\x89\xe5\xad\x98'.decode('utf-8', errors='ignore'))
print(len('中文'.encode('utf-8')))

print('大家好，我是%s ,今天給大家带来一首%s' % ('小傻瓜', '难听的歌'))
print('大家好，我是%s ,今天給大家带来一首%s' % ('小傻瓜', 888))

s1 = 72
s2 = 85
print('进步了%s' % ((85-72)*100 // 72)+'%')
