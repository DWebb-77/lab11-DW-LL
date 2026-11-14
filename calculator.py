# https://github.com/DWebb-77/lab11-DW-LL.git
# Partner 1: Dylan Webb
# Partner 2: Lucas Lyle

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot be negative")

    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

# First example
def add(a, b):
    return a + b

def subtract(a, b):
    return a -b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero: 'a' cannot be 0.")
    return b / a

def logarithm(a, b):
    if a < 0:
        raise ValueError("Invalid base")
    if a == 1:
        raise ValueError("Invalid base")
    if b <= 0:
        raise ValueError("Invalid input")

    return math.log(b, a)

def exp(a, b):
    return a ** b
