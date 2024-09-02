#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Print only the arguments passed via command line, excluding the script name
for arg in sys.argv[1:]:
    print(arg)

# Calculate the factorial of the first argument if provided
if len(sys.argv) > 1:
    try:
        number = int(sys.argv[1])
        f = factorial(number)
        print(f"Factorial of {number} is {f}")
    except ValueError as e:
        print(f"Error: {e}")
