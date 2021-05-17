#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # dict seems to be more readable
    animals = dict(kitten = 'asdf', puppy = 'asdf', lion='sadfaa', giraffe = 'asdfxz')
    # animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
    #     'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    for k in animals.keys(): print(k)
    for v in animals.values(): print(v)
    animals['lion'] = 'this is a lion' 
    animals['monkey'] = 'haha' # add a new item with key 'monkey'
    print("FOUND!" if "asdf" in animals else "Not found!")
    print_dict(animals)

def print_dict(o):
    for k, v in o.items():
        print(f"{k}: {v}")

if __name__ == '__main__': main()
