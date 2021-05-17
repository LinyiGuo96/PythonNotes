#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.'.upper())


print('Hello, World.'.lower())

print('Hello, World.'.swapcase())

print('Hello, World.{}'.format(42*7))

print('''
Hello, 
World.
{}'''.format(42*7))


class Mystring(str):
    def __str__(self):
        return self[::-1]

s = Mystring("hello")
print(s)