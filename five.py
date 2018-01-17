#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import time


def one(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError('不是数字')
    print(a)
    print(b)
    return a, b


def two():
    pass


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('类型错误')
    elif not isinstance(b, (int, float)):
        raise TypeError('类型错误')
    elif not isinstance(c, (int, float)):
        raise TypeError('类型错误')
    print('-----开始计算-----')
    t1 = time.time()
    if b * b - 4 * a * c < 0:
        print('此方程无解')
        return
    d = math.sqrt((b * b) - (4 * a * c))
    j1 = (-b + d) / (2 * a)
    j2 = (-b - d) / (2 * a)
    t2 = time.time()

    return j1, j2


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def list_add(ll=None):
    if ll is None:
        ll = []
    ll.append('end')
    return ll


def calc(*number):
    sums = 0
    for num in number:
        sums = sums + num * num

    return sums


if __name__ == "__main__":
    print(calc(1, 2, 3))
    numlist = [2, 3, 4]
    print(calc(*numlist))
