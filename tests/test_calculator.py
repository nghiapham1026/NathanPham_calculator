from calculator import *
import random

# Basic operations
print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))

# Advanced operations
print(power(2, 3))

# Logarithms
print(log(100))

# Trigonometry
print(sine(30))

# Generate random numbers
num1 = random.randint(1, 100)  # Random integer between 1 and 100
num2 = random.randint(1, 100)  # Another random integer between 1 and 100

# Basic operations
print(f"add({num1}, {num2}) = {add(num1, num2)}")
print(f"subtract({num1}, {num2}) = {subtract(num1, num2)}")
print(f"multiply({num1}, {num2}) = {multiply(num1, num2)}")

# Ensure num2 is not zero for division
if num2 != 0:
    print(f"divide({num1}, {num2}) = {divide(num1, num2)}")

# Advanced operations
exp_val = random.randint(1, 10)  # Random exponent between 1 and 10
print(f"power({num1}, {exp_val}) = {power(num1, exp_val)}")

# Generate a random number for testing exponential function
num = random.uniform(1, 10)  # Random float between 1 and 10

# Test exponential function
print(f"exponential({num}) = {exponential(num)}")

# Test power function for comparison
base = random.randint(2, 5)
exponential_val = random.randint(1, 3)
print(f"power({base}, {exponential_val}) = {power(base, exponential_val)}")

# Logarithms (logarithm of num1)
if num1 > 0:
    print(f"log({num1}) = {log(num1)}")

# Trigonometry (random angle between 0 and 360)
angle = random.randint(0, 360)
print(f"sine({angle}) = {sine(angle)}")

# Factorial (random number between 0 and 10)
factorial_num = random.randint(0, 10)
print(f"factorial({factorial_num}) = {factorial(factorial_num)}")

# Generate a random dataset of 20 numbers between 1 and 100
random_data = [random.randint(1, 100) for _ in range(20)]

# Display the random dataset
print(f"Random dataset: {random_data}")

# Test mean
print(f"Mean of data: {mean(random_data)}")

# Test median
print(f"Median of data: {median(random_data)}")

# Test mode
try:
    print(f"Mode of data: {mode(random_data)}")
except Exception as e:
    print(f"Error finding mode: {e}")

# Test standard deviation
print(f"Standard Deviation of data: {standard_deviation(random_data)}")
