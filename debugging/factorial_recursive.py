#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a number using recursion.

    Parameters:
        n (int): A non-negative integer

    Returns:
        int: The factorial of the input number
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
