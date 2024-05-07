#!/usr/bin/python3
import sys

def factorial(n):
    """Calculate the factorial of a given number recursively"""
    # Parameters:
    #   n (int): An integer for which factorial is to be calculated.
    #
    # Returns:
    #   int: The factorial of the input integer.
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Check if command-line argument is provided
if len(sys.argv) < 2:
    print("Usage: python3 factorial_recursive.py <number>")
    sys.exit(1)

# Usage of the function:
# Take the command-line argument and calculate its factorial using the factorial function.
try:
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:
    print("Please provide a valid integer as argument.")
