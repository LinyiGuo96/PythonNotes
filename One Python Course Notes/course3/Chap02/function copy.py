#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def function(n = 1):
    print(n)

function(47)

function()

x = function(100) # wrong
# print(x) # wrong, function doesn't have 'return'
