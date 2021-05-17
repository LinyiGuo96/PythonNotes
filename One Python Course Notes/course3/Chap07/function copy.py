#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# def main():
#     kitten()

# def kitten(n=1):
#     print(f'Meow.{n}')

# if __name__ == '__main__': main()


def main():
    x = kitten()
    print(x) # all functions return a value. if you don't name it then you will get 'None'.

def kitten():
    print('Meow.')
    return 'Meow....'

if __name__ == '__main__': main()
