#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    sound = "Quaaack!"
    walking = "Walks like a duck."

    def quack(self): # 'self' is always the first element 
        #print('Quaaack!')
        print(self.sound)
    def walk(self):
        #print('Walks like a duck.')
        print(self.walking)


def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()
