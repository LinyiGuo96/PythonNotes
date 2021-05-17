#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# def f1():
#     print("this is f1")

# x = f1 
# x()

def f1(f): # take a function as the argument
    def f2():
        print("this is before the function call")
        f()
        print("this is after the function call")
    return f2

def f3():
    print("this is f3")

f3 = f1(f3)
f3()


# but we usually use the decorator

def f1(f): # take a function as the argument
    def f2():
        print("this is before the function call")
        f()
        print("this is after the function call")
    return f2

@f1 # this syntax is the sign of the decorator, in this case f3 is our decorator
# it will take the function below as the input 
def f3():
    print("this is f3")


# check the decorator.py