"""
3 Strikes
Given an integer between 1 and 10,000, return a count of how many numbers from 1 up to that integer whose square contains
at least one digit 3.

1. squares_with_three(1) should return 0.
2. squares_with_three(10) should return 1.
3. squares_with_three(100) should return 19.
4. squares_with_three(1000) should return 326.
5. squares_with_three(10000) should return 4531.
"""

def squares_with_three(n: int) -> int:
    counter = 0

    for i in range(n+1):
        if "3" in str(i**2):
            counter += 1

    return counter


print(squares_with_three(1))
print(squares_with_three(10))
print(squares_with_three(100))
print(squares_with_three(1000))
print(squares_with_three(10000))
