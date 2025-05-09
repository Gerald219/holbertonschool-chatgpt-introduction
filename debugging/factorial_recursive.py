#!/usr/bin/python3
import sys

def factorial(n):
    """
    1. What it does:
       Uses recursion to calculate the factorial of a number.
       Basically, it multiplies the number by everything below it (n * n-1 * n-2...).

    2. Parameter:
       n (int): A number greater than or equal to 0. This is the number we're finding the factorial of.

    3. Returns:
       int: The result of multiplying n by every number below it down to 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
