#!/usr/bin/python3
import sys

def factorial(n):
    """
    Computes the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the integer n. If n is 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
