"""
Pocket Change
Given an array of integers representing the coins in your pocket, with each integer being the value of a coin in cents,
return the total amount in the format "$D.CC".

100 cents equals 1 dollar.
In the return value, include a leading zero for amounts less than one dollar and always exactly two digits for the cents.

1. count_change([25, 10, 5, 1]) should return "$0.41".
2. count_change([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25]) should return "$1.43".
3. count_change([100, 25, 100, 1000, 5, 500, 2000, 25]) should return "$37.55".
4. count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10]) should return "$0.70".
5. count_change([1]) should return "$0.01".
6. count_change([25, 25, 25, 25]) should return "$1.00".
"""

def count_change(change: list[int]) -> str:
    return f"${sum(change) / 100:.2f}"


print(count_change([25, 10, 5, 1]))
print(count_change([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25]))
print(count_change([100, 25, 100, 1000, 5, 500, 2000, 25]))
print(count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10]))
print(count_change([1]))
print(count_change([25, 25, 25, 25]))
