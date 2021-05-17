#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import Decimal

x = 7
print('x is {}'.format(x))
print(type(x))

x = 7 * 3
print('x is {}'.format(x))
print(type(x))

x = 7 / 3
print('x is {}'.format(x))
print(type(x))

x = 7 // 3
print('x is {}'.format(x))
print(type(x))

x = 7.0
print('x is {}'.format(x))
print(type(x))

x = .1 + .1 + .1 - .3
print('x is {}'.format(x))
print(type(x))

a = Decimal(".1")
b = Decimal(".3")
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))
