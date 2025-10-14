"""
Factorializer
Given an integer from zero to 20, return the factorial of that number. The factorial of a number is the product of all
the numbers between 1 and the given number.

The factorial of zero is 1.
1. factorial(0) should return 1.
2. factorial(5) should return 120.
3. factorial(20) should return 2432902008176640000.
"""

def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(0))
print(factorial(5))
print(factorial(20))
