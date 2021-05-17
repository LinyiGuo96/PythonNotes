#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import os 

print(os.getcwd())

def main():
    f = open('Chap12\lines.txt', "r") 
    # 'w' write the mode
    # 'a' append
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()
