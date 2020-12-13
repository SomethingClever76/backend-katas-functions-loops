#!/usr/bin/env python
"""Implements math functions without using operators,
except for '+' and '-'.
"""

__author__ = "Kyle Thomas"


def add(x, y):
    """Add two integers."""
    # your code here
    # print(x + y)
    return x + y


# add(2, 4)


def multiply(x, y):
    """Multiply x with y using the add() function above."""
    # your code here
    # total acts as an accumulator
    total = 0

    # for x, y - find the higher abs() value:
    # then use the add() function abs(higher number) of times
    # while subtracting abs(higher number) each time
    if abs(x) > abs(y):
        for i in range(0, abs(x)):
            total -= add(abs(x), abs(y)) - abs(x)
    else:
        for i in range(0, abs(y)):
            total -= add(abs(x), abs(y)) - abs(y)

    # determine whether total returned should be positive or negative:
    # when both numbers are negative or both numbers are positive:
    #   the total is always positive
    # if one of the two numbers is negative:
    #   the total will be negative
    if x < 0 and y < 0 or x > 0 and y > 0:
        # print(abs(total))
        return abs(total)
    else:
        # print(total)
        return total


# multiply(6, -8)


def power(x, n):
    """Raise x to power n, where n >= 0, using the functions above."""
    # your code here
    # loop variable used to control number of iterations
    loop_var = 0
    # accumulator
    total = 1

    while loop_var != n:
        total = multiply(x, total)
        # increment the loop variable
        loop_var = add(loop_var, 1)

    # when loop is complete, print/return the total
    # print(total)
    return total


# power(2, 8)


def factorial(x):
    """Compute the factorial of x, where x > 0, using the functions above."""
    # your code here
    return


def fibonacci(n):
    """Compute the nth term of fibonacci sequence using the functions above."""
    # your code here
    return


if __name__ == '__main__':
    # your code to call functions above
    pass
