"""
Pascal's Triangle Row
Given an integer n, return the nth row of Pascal's triangle as an array.

In Pascal's Triangle, each row begins and ends with 1, and each interior value is the sum of the two values directly above it.

Here's the first 5 rows of the triangle:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

1. pascalRow(5) should return [1, 4, 6, 4, 1].
2. pascalRow(3) should return [1, 2, 1].
3. pascalRow(1) should return [1].
4. pascalRow(10) should return [1, 9, 36, 84, 126, 126, 84, 36, 9, 1].
5. pascalRow(15) should return [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1].
"""

def pascal_row(n: int) -> list[int]:
    row: list[int] = [1]

    for i in range(1, n):
        row.append(row[-1] * (n - i) // i)

    return row


print(pascal_row(5))
print(pascal_row(3))
print(pascal_row(1))
print(pascal_row(10))
print(pascal_row(15))
