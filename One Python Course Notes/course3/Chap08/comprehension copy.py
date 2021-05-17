#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import math


def main():
    # print(math.pi)
    seq = range(11)
    seq2 = [x for x in seq if x % 3 != 0]
    seq2 = [(x, x**2) for x in seq]
    seq2 = [round(math.pi, i) for i in seq]
    seq2 = {x: x**2 for x in seq} # use print
    seq2 = {x for x in "superduper" if x not in "pd"} # use print
    print_list(seq)
    print(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()
