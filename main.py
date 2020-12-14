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

    # For x, y - find the higher abs() value:
    # then use the add() function abs(higher number) of times
    # while subtracting abs(higher number) each time.
    if abs(x) > abs(y):
        for i in range(0, abs(x)):
            total -= add(abs(x), abs(y)) - abs(x)
    else:
        for i in range(0, abs(y)):
            total -= add(abs(x), abs(y)) - abs(y)

    # Determine whether total returned should be positive or negative:
    #    when both numbers are negative or both numbers are positive:
    #        the total is always positive
    #    if one of the two numbers is negative:
    #        the total will be negative
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

    # Since we are told that n will be >= 0, we aren't concerned
    # with negative exponentiation. Since the 0th power of any number is 1,
    # total is initialized to a value of 1. If n is 0, we simply return that 1.
    # Otherwise, the first iteration is (x * 1).
    # For example power(2, 3) would start as
    # loop_var is 0    (2 * 1)    total is now 2
    # loop_var is 1    (2 * 2)    total is now 4
    # loop_var is 2    (2 * 4)    total is now 8
    # loop_var is 3, which is equal to the value of "n" in this example.
    # loop is ended and final total is returned.
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
    # accumulator
    total = x

    # Taking factorial(4) as an example,
    # we are not doing this - (4 * 3 * 2 * 1).
    # Instead, we are making use of the commutative property of multiplication.
    # i is 1    (4 * 1) is how we start   total is now 4
    # i is 2    (4 * 2) is next           total is now 8
    # i is 3    (8 * 3) final loop        total is now 24
    # Since we passed in x as our stop position in the range() function,
    # the loop stops here and the final total is 24.
    # (Special Condition - we check whether x is 0 or 1 because the
    # factorial for both is 1)
    if x == 0 or x == 1:
        return 1
    else:
        for i in range(1, x):
            total = multiply(total, i)

    # when loop is complete, print/return the total
    # print(total)
    return total


# factorial(4)


def fibonacci(n):
    """Compute the nth term of fibonacci sequence using the functions above."""
    # your code here
    # accumulator/sequence starts at 0
    total = 0
    # keep track of previous numbers to be added to total
    prev1 = 0
    prev2 = 1

    # Using total_list just to make sure numbers are correct
    # should be: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...]
    total_list = []
    # if n == 1:
    #     total = 1
    # else:
    #     for i in range(1, n):
    #         total = add(prev1, prev2)
    #         prev1 = prev2
    #         prev2 = total
    for i in range(n + 1):
        total = add(total, prev1)
        total_list.append(total)
        prev1 = prev2
        prev2 = total
    print("fib list looks like:", total_list)
    print(f"if n is {n}\n", "fib number is", total, '\n')
    return total


fibonacci(0)
fibonacci(1)
fibonacci(2)
fibonacci(3)
# fibonacci(4)
# fibonacci(5)
# fibonacci(6)
# fibonacci(7)
# fibonacci(8)


if __name__ == '__main__':
    # your code to call functions above
    pass
