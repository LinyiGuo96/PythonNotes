#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# def main():
#     try :
#         #x = int("foo")
#         x = 5/1
#     except ValueError:
#         print("it's a value error!")
#     except ZeroDivisionError:
#         print("Devide by 0!")
#     else: 
#         print("Good JOb")
#         print(x)
# if __name__ == '__main__': main()



import sys

def main():
    try :
        #x = int("foo")
        x = 5/0
    except ValueError:
        print("it's a value error!")
    except:
        print(f"Unknown error: {sys.exc_info()[1]}")
    else: 
        print("Good JOb")
        print(x)
if __name__ == '__main__': main()
