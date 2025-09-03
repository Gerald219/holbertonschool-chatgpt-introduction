#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a number n.

    Args:
        n (int): A positive integer.
    Returns:
        int: The factorial of n.
    """
    if n < 0:
        raise ValueError("n must be >= 0")

    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)

