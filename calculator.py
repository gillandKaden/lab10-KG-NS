"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math

def hypotenuse(a, b):
    try:
        math.hypot(a, b) # can have negative nums
    except ValueError:
        raise ValueError

def square_root(a):
    return a ** 0.5

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError


def logarithm(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        raise ValueError

def exp(a, b):
    return a ** b





