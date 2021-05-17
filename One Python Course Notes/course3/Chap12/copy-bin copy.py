#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('Chap12/berlin.jpg', 'rb') # b: binary
    outfile = open('Chap12/berlin-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240) # 10 kbytes
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
