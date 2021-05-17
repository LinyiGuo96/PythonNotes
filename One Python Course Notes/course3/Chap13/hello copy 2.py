#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = (1,2,3,4,5)
y = x
print(y)

y = reversed(x)
print(y)
y = list(y)
print(y)

# max(), min()

y = (6,7,8,9,10)

z = zip(x,y)
for a,b in z: print(f"{a} - {b}")


x = ("cat", "dog", "lobster")
for i, v in enumerate(x): print(f"{i}, {v}")
# i will be the order
# this could be useful to get the ordered things
