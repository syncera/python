#!/usr/bin/env python3
#sincera

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 2) + fib(n - 1)

calc = int(input("What number to calculate?? "))
print(fib(calc))