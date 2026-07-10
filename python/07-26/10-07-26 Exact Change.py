"""
Exact Change
Given an integer amount in cents, return the number of distinct ways to make exact change using pennies (1 cent),
nickels (5 cents), dimes (10 cents), and quarters (25 cents).

1. exact_change(3) should return 1.
2. exact_change(9) should return 2.
3. exact_change(17) should return 6.
4. exact_change(39) should return 24.
5. exact_change(61) should return 73.
6. exact_change(99) should return 213.
"""

def exact_change(amount: int) -> int:
    ways: list[int] = [0] * (amount + 1)
    ways[0] = 1
    coins: list[int] = [1, 5, 10, 25]

    for coin in coins:
        for current_amount in range(coin, amount + 1):
            ways[current_amount] += ways[current_amount - coin]

    return ways[amount]


print(exact_change(3))
print(exact_change(9))
print(exact_change(17))
print(exact_change(39))
print(exact_change(61))
print(exact_change(99))
