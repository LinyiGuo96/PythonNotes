#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    infile = open('Chap12/lines.txt', 'rt') # read and text mode
    outfile = open('Chap12/lines-copy.txt', 'wt') # write and text mode
    for line in infile:
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)
    outfile.close() # prevent from losing data
    print('\ndone.')

if __name__ == '__main__': main()
