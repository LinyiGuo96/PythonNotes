#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import time

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
    return wrapper


@elapsed_time
def big_sum():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')
# now the big_sum() has been decorated to the elapsed_time(f) function

def main():
    big_sum() # note we used big_sum() here!

if __name__ == '__main__': main()
