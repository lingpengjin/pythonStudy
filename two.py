#!/usr/bin/env python3
# -*- coding: utf-8 -*-
onelist = ['one', 'two', 'three', 'four', 'five']
print(onelist)
print(len(onelist))
print(onelist[-1])
onelist.append('six')
print(onelist)
onelist.insert(0, 'seven')
print(onelist)
onelist.pop()
print(onelist)
onelist.pop(0)
print(onelist)
twolist = [1, 2, 3, [4, 5, 6], onelist]
print(twolist)
print(len(twolist))
threelist = (2, 2, 2, 2, onelist)
print(threelist)
onelist.append('eight')
print(threelist)
print(threelist[4][1])
fourlist = [3, 3]
