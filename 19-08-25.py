"""
Sum of Squares
Given a positive integer up to 1,000, return the sum of all the integers squared from 1 up to the number.

1. sum_of_squares(5) should return 55.
2. sum_of_squares(10) should return 385.
3. sum_of_squares(25) should return 5525.
4. sum_of_squares(500) should return 41791750.
5. sum_of_squares(1000) should return 333833500.
"""

def sum_of_squares(n: int) -> int:
    squared_sums: list[int] = []

    for i in range(n+1):
        squared_sums.append(i**2)

    return sum(squared_sums)


print(sum_of_squares(5))
print(sum_of_squares(10))
print(sum_of_squares(25))
print(sum_of_squares(500))
print(sum_of_squares(1000))
