#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = '7.0'
print('x is {}'.format(x))
print(type(x))

# int, float, str, bool(T/F), NoneType 

x = '''
seven
five
dog
'''
print("x is {}".format(x))
print(type(x))  # ''' ** ''' multi-line str


x = 'seven'.capitalize() # upper() and lower()
print('x is {}'.format(x))
print(type(x))

# 'seven' is an object!


x = '7.0  {} {}'.format(5,6) # the order is the same
print('x is {}'.format(x))
print(type(x))


x = '7.0  {1} {0}'.format(5,6) # chagne the order
print('x is {}'.format(x))
print(type(x))

x = '7.0  "{1:<09}" "{0:>09}"'.format(5,6) # check what will happen
print('x is {}'.format(x))
print(type(x))

a = 5 
b = 6
x = f'7.0  {a:<09} {b:>09}'
print('x is {}'.format(x))
print(type(x))