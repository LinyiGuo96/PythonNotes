#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# def main():
#     kitten('meow', 'grrr', 'purr')

# def kitten(*args): # variable length argument list
#     if len(args):
#         for s in args:
#             print(s)
#     else: print('Meow.')

# if __name__ == '__main__': main()

def main():
    x = ('meow', 'grrr', 'purr', "asdfas", "adsf")
    kitten(*x)

def kitten(*args): # variable length argument list
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')








if __name__ == '__main__': main()


