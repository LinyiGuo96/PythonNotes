#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73

if x < y:
    z= 100
    print('x < y: x is {} and y is {}'.format(x, y))
else:
    print('x > y: x is {} and y is {}'.format(x, y))

print("something else. {}".format(z))


x = 100
y = 100

if x < y:
    z= 100
    print('x < y: x is {} and y is {}'.format(x, y))
elif x > y:
    print('x > y: x is {} and y is {}'.format(x, y))
else:
    print("x=y={}".format(x))
