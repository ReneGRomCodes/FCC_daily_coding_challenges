"""
Tip Calculator
Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom
amount.

Prices will be given in the format: "$N.NN".
Custom tip percents will be given in this format: "25%".
Return amounts in the same "$N.NN" format, rounded to two decimal places.
For example, given a "$10.00" meal price, and a "25%" custom tip value, return ["$1.50", "$2.00", "$2.50"].

1. calculate_tips("$10.00", "25%") should return ["$1.50", "$2.00", "$2.50"].
2. calculate_tips("$89.67", "26%") should return ["$13.45", "$17.93", "$23.31"].
3. calculate_tips("$19.85", "9%") should return ["$2.98", "$3.97", "$1.79"].
"""

def calculate_tips(meal_price: str, custom_tip: str) -> list[str]:
    meal_price: float = float(meal_price[1:])
    custom_tip: int = int(custom_tip[:-1])
    tip_values: tuple[int, ...] = (15, 20, custom_tip)

    prices_with_tip: list[str] = []

    for v in tip_values:
        prices_with_tip.append(f"${round(meal_price/100*v, 2)}")

    return prices_with_tip


print(calculate_tips("$10.00", "25%"))
print(calculate_tips("$89.67", "26%"))
print(calculate_tips("$19.85", "9%"))
