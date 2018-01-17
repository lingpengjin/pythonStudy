#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


def nvn():
    num = input('输入数字：\n')
    n = random.randint(0, 9)
    if int(num) >= n:
        print('You WiN')
    else:
        print('You LOSE')


def game():
    nvn()
    while True:
        a = input('是否继续? (y/n)\n')
        if a == 'y':
            nvn()
        else:
            print('游戏结束')
            break




# print('开始游戏')
# game()

print(list(range(4, 100)))
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hi %s' % name)
