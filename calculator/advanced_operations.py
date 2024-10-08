import math

def power(base, exp):
    return base ** exp

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number")
    return x ** 0.5

def factorial(n):
    if n < 0:
        raise ValueError("Cannot compute the factorial of a negative number")
    if n == 0 or n == 1:
        return 1
    return math.factorial(n)