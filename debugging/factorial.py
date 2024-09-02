#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("The factorial is not defined for negative numbers")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Please provide exactly one argument")
        n = int(sys.argv[1])
        f = factorial(n)
        print(f)
    except ValueError as e:
        print(f"Error : {e}")
