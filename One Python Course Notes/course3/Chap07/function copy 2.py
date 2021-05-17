#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# def main():
#     kitten(5,6,7)

# def kitten(a, b, c):
#     print('Meow.')
#     print(a,b,c)
# if __name__ == '__main__': main()


# def main():
#     kitten(5,6)

# def kitten(a, b, c=1):
#     print('Meow.')
#     print(a,b,c)
# if __name__ == '__main__': main()


# def main():
#     x=5
#     kitten(x)
#     print(f"in main: x is {x}")

# def kitten(a):
#     print('Meow.')
#     print(a)
# if __name__ == '__main__': main()


def main():
    x = 5 # integer is immutable
    y = x
    y = 3
    print(id(x))
    print(id(y))
    print(x)
    print(y)

    a = [5] # list is mutable
    b = a
    b[0] = 3
    print(id(a))
    print(id(b))
    print(a)
    print(b)
    # kitten(x)
    print(f"in main: x is {x}")

def kitten(a):
    print('Meow.')
    print(a)
if __name__ == '__main__': main()
