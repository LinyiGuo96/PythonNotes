#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x=123

print('Hello, World. {}'. format(x)) #python3
print('Hello, World. %d' %x) # python2, will be removed in the future perhaps
print(f'Hello. {x}')