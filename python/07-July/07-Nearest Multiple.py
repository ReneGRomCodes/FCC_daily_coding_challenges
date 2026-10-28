"""
Nearest Multiple
Given two integers, round the first to the nearest multiple of the second.

1. round_to_nearest_multiple(5, 3) should return 6.
2. round_to_nearest_multiple(17, 4) should return 16.
3. round_to_nearest_multiple(43, 5) should return 45.
4. round_to_nearest_multiple(38, 11) should return 33.
5. round_to_nearest_multiple(93, 12) should return 96.
"""

def round_to_nearest_multiple(num: int, multiple: int):
    multiplicator: int = 2
    lower_product: int = multiple
    higher_product: int = multiple * multiplicator

    # Find the products of 'multiple' that are directly lower and higher than 'num'.
    while num > higher_product:
        multiplicator += 1
        lower_product = multiple * multiplicator
        higher_product = multiple * (multiplicator + 1)

    if abs(num - lower_product) < abs(num - higher_product):
        return lower_product
    else:
        return higher_product


print(round_to_nearest_multiple(5, 3))
print(round_to_nearest_multiple(17, 4))
print(round_to_nearest_multiple(43, 5))
print(round_to_nearest_multiple(38, 11))
print(round_to_nearest_multiple(93, 12))
