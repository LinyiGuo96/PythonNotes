#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys

import os 
# try 
# os.name os.getenv('PATH'), os.getcwd(), os.urandom(25).hex() (random number)

import random

# def main():
#     v = sys.version_info
#     print('Python version {}.{}.{}'.format(*v))



# def main():
#     v = sys.platform
#     i = os.name
#     print(v)
#     print(i)

# def main():
#     x = random.randint(1,100) # between 1 and 100
#     y = list(range(25))
#     print(x)
#     random.shuffle(y)
#     print(y)
# if __name__ == '__main__': main()

import datetime

def main():
    now = datetime.datetime.now()
    print(now.year, now.month, now.day)


if __name__ == '__main__': main()