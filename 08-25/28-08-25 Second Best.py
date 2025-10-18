"""
Second Best
Given an array of integers representing the price of different laptops, and an integer representing your budget, return:

The second most expensive laptop if it is within your budget, or
The most expensive laptop that is within your budget, or
0 if no laptops are within your budget.
Duplicate prices should be ignored.

1. get_laptop_cost([1500, 2000, 1800, 1400], 1900) should return 1800
2. get_laptop_cost([1500, 2000, 2000, 1800, 1400], 1900) should return 1800
3. get_laptop_cost([2099, 1599, 1899, 1499], 2200) should return 1899
4. get_laptop_cost([2099, 1599, 1899, 1499], 1000) should return 0
5. get_laptop_cost([1200, 1500, 1600, 1800, 1400, 2000], 1450) should return 1400
"""

def get_laptop_cost(laptops: list[int], budget: int) -> int:
    laptops.remove(max(laptops))  # Remove most expensive Laptop first.
    found_laptop = False

    while not found_laptop:
        if laptops:
            if max(laptops) > budget:
                laptops.remove(max(laptops))
                continue
            elif max(laptops) <= budget:
                found_laptop = max(laptops)

        else:
            return 0

    return found_laptop


print(get_laptop_cost([1500, 2000, 1800, 1400], 1900))
print(get_laptop_cost([1500, 2000, 2000, 1800, 1400], 1900))
print(get_laptop_cost([2099, 1599, 1899, 1499], 2200))
print(get_laptop_cost([2099, 1599, 1899, 1499], 1000))
print(get_laptop_cost([1200, 1500, 1600, 1800, 1400, 2000], 1450))
