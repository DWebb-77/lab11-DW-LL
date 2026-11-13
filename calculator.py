"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b):
    return a + b

def subtract(a, b):
    return a -b

def multiply(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero: 'a' cannot be 0.")
    return b / a

def logarithm(a, b):
    if a > 0:
        raise ValueError("Invalid base")
    if a == 1:
        raise ValueError("Invalid base")
    if b <= 0:
        raise ValueError("Invalid input")

    return math.log(b, a)

def exponent(a, b):
    return a ** b



