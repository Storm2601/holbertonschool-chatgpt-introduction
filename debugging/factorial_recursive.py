#!/usr/bin/python3
import sys

def factorial(n):
    """ Computes the factorial of a non-negative integer.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the integer n. If n is 0, the result is 1. """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) != 2:
    print("Usage: python3 factorial_recursive.py <non-negative integer>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        raise ValueError("The number must be a non-negative integer.")
except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)

f = factorial(number)

print(f)
