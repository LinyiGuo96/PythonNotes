#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')


x = 1234
print(f"{x} is our number.")

y = 4321
print(f"{x} and {y}!")

print(f"The inverse of {x} is {y}!")

print("{1} and {0}!".format(x,y))

print("{0:<5} and {1:>+08}!".format(x,y))

x = 1214 * 13 *321

print("the numebr is {:,}".format(x))
print("the numebr is {:,}".format(x).replace(",", "."))

x = 1234
print("the numebr is {:.3f}".format(x))
print("the number is {:b}".format(x)) #binary

