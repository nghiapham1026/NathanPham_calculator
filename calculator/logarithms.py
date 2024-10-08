import math

def log(x, base=10):
    if x <= 0:
        raise ValueError("Logarithm undefined for zero or negative numbers")
    return math.log(x, base)

def ln(x):
    return log(x, math.e)

def exponential(x):
    return math.exp(x)