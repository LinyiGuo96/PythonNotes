#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [ 1, 2, 3, 4, 5 ] #list
for i in x:
    print('i is {}'.format(i))

x[4] = 100
for i in x:
    print(f'i is {i}')

x = range(10)
for i in x:
    print('i is {}'.format(i))

x = range(5, 10)
for i in x:
    print('i is {}'.format(i))

x = range(1, 10, 2) # range cannot be changed, like tuples, they are immutable
for i in x:
    print('i is {}'.format(i))

x = list(range(1, 10, 2))
x[2] = 100
for i in x:
    print('i is {}'.format(i))

x = {'one': 1, 'two':2, 'three': 3} #dict
for i in x:
    print('i is {}'.format(i))
x['two'] = 100
for k,v in x.items():
    print('k: {}, v: {}'.format(k, v))
