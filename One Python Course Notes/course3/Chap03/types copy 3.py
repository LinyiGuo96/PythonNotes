#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = True
print('x is {}'.format(x))
print(type(x)) # bool

x = 7 > 5
print('x is {}'.format(x))
print(type(x))

x = None
print('x is {}'.format(x))
print(type(x))

x=1
if x :
    print("True")
else:
    print("False") # None, 0, empty str are False