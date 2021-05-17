#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'

if a and b:
    print('expression is true')
else:
    print('expression is false')

if not a:
    print('expression is true')
else: 
    print('expression is F')

if y in x:
    print("It's true!")

if y is x[0]:
    print(f"x contains {y}")
else:
    print("Nope")

if 'tree' in x:
    print("It's true!")

if y is x[0]: # their id is the same
    print(f"{y} is x[0].")
else:
    print(f"{y} is not x[0].")

