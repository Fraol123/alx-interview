#!/usr/bin/python3
'''
calculates the minimum amount of processes necessary
to create a certain number of characters.
You must imagine that there is only one function
to copy everything and one to paste.
'''


def minOperations(n):
    p = 0

    if n <= 1:
        return p

    for i in range(2, n + 1):
        while (0 == n % i):
            p = p + i
            n = n / i
            if n < i:
                break
    return p
