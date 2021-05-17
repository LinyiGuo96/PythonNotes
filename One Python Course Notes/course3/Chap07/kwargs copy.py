#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')

def kitten(**kwargs): 
    # kwargs: key word arguments, like args, this name is just a convention
    # ** for dict
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__': main()
