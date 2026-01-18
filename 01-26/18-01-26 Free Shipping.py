"""
Free Shipping
Given an array of strings representing items in your shopping cart, and a number for the minimum order amount to qualify
for free shipping, determine if the items in your shopping cart qualify for free shipping.

The given array will contain items from the list below:

Item	 Price
"shirt"	 34.25
"jeans"	 48.50
"shoes"	 75.00
"hat"	 19.95
"socks"	 15.00
"jacket" 109.95

1. gets_free_shipping(["shoes"], 50) should return True.
2. gets_free_shipping(["hat", "socks"], 50) should return False.
3. gets_free_shipping(["jeans", "shirt", "jacket"], 75) should return True.
4. gets_free_shipping(["socks", "socks", "hat"], 75) should return False.
5. gets_free_shipping(["shirt", "shirt", "jeans", "socks"], 100) should return True.
6. gets_free_shipping(["hat", "socks", "hat", "jeans", "shoes", "hat"], 200) should return False.
"""

def gets_free_shipping(cart: list[str], minimum: int) -> bool:
    item_prices: dict[str, float] = {
        "shirt": 34.25,
        "jeans": 48.50,
        "shoes": 75.00,
        "hat": 19.95,
        "socks": 15.00,
        "jacket": 109.95,
    }

    return sum([item_prices[x] for x in cart]) >= minimum


print(gets_free_shipping(["shoes"], 50))
print(gets_free_shipping(["hat", "socks"], 50))
print(gets_free_shipping(["jeans", "shirt", "jacket"], 75))
print(gets_free_shipping(["socks", "socks", "hat"], 75))
print(gets_free_shipping(["shirt", "shirt", "jeans", "socks"], 100))
print(gets_free_shipping(["hat", "socks", "hat", "jeans", "shoes", "hat"], 200))
