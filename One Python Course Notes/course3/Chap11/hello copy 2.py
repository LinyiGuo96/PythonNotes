#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.'.capitalize())

print('Hello, World.'.title())

print('Hello, World.'.casefold())

# note: string is immutable 

s1 = "hello"
s2 = s1.upper()
s3 = "world"
print(id(s1))
print(id(s2))

print(s1 + " " + s3)

# Or

s4 = 'this one' ' that one'
print(s4)

