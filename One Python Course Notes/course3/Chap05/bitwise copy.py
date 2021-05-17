#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 0x0a
y = 0x02
z = x & y # and: common
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}') # hexadecimal(x): 0-15(16 jin zhi)
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')



x = 0x0a
y = 0x05
z = x | y # Or
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}') 
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')


x = 0x0a
y = 0x0f
z = x ^ y # only those contained in one object
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}') 
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')


x = 0x0a
y = 0x01
z = x << y #shift left
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}') 
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

x = 0x0a
y = 0x01
z = x >> y #shift right
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}') 
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
