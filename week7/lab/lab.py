
import math


def print_reversed(n):
    if 0 < n:
        print(n)
        n -= 1
        return print_reversed(n)



print_reversed(3)


def rec_sum_helper(n):
    return n

def rec_sum(n):
    if 0 > n:
        return 0
    return n + rec_sum(n-1)

print(rec_sum(5))

def rec_multy(n):
    if 0 > n:
        return 0
    return n * rec_sum(n-1)


def exp_n_x(n, x):
    if n < 0:
        return None
    if n < 1:
        return 1
    return (x**n/math.factorial(n)) + exp_n_x(n-1 , x)

