#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class bunny:
    def __init__(self, n):
        self._n = n
    def __repr__(self):
        return f'repr: the number is {self._n} 🖖'
        # repr
    def __str__(self):
        return f'str: the number is {self._n}'
        # string 

s = bunny(33)
print(s) # str is the default!
print(repr(s))
print(ascii(s)) # works as repr, but can output emoji!

print(chr(128406))
print(ord('🖖'))