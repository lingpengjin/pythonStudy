#!/usr/bin/env python3
# -*- coding: utf-8 -*-

onedict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
print('fff', onedict.get('five',False))
print(onedict)
print(onedict['one'])
onedict['five'] = 5
onedict['five'] = 6
print(onedict)
a= 2
onelist = ['one', 'five', 'six', 'seven']
twolist = ['one', 'two', 'three', a, 'eight']
threeset = set(twolist)
threeset.add('five')
threeset.remove('two')
a = 3
print(threeset)
print(a)
print('one' in threeset)
for three in threeset:
    print(three)