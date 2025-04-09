"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b): a + b

def subtract(a, b): a - b

def multiply(a, b): a * b

def divide(a, b):

    try:
        if a == 0:
            raise ZeroDivisionError
        b / a   # raise ZeroDivisionError if a == 0
    except ValueError:
        print("Number cannot be zero")
def logarithm(a, b):
    try:
        if b <= 0:
            raise ValueError
        math.log(a,b) # use math library + try/catch
    except ValueError:
        print("Base cannot be less than zero")
def exponent(a, b):
    a ** b       # use math library + try/catch



