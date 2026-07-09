"""
Max Profit
Given an array of daily stock prices and a budget (in dollars), calculate the maximum profit you could make by buying
and selling the stock over the given period.

- You may only sell after you buy.
- You can only buy whole shares.
- Return the maximum possible profit as a string, rounded down to the nearest cent and formatted to two decimal places.

1. get_max_profit([5, 6], 50) should return "10.00".
2. get_max_profit([8, 2, 5, 10], 20) should return "80.00".
3. get_max_profit([4, 5, 3, 6], 20) should return "18.00".
4. get_max_profit([54.40, 51.22, 53.99, 50.28, 53.01, 52.84], 200) should return "8.31".
5. get_max_profit([15.38, 15.01, 14.99, 14.62, 14.28], 80) should return "0.00".
6. get_max_profit([121.45, 126.82, 122.91, 124.65, 128.83, 128.83, 127.33], 1230.25) should return "73.80".
"""

def get_max_profit(prices: list[float], budget: float) -> str:
    max_profit: float = 0.0
    max_price_seen: float = 0.0

    for current_buy_price in reversed(prices):
        if current_buy_price > max_price_seen:
            max_price_seen = current_buy_price

        shares_to_buy: int = int(budget / current_buy_price)

        if shares_to_buy == 0:
            continue

        potential_profit: float = (max_price_seen - current_buy_price) * shares_to_buy

        if potential_profit > max_profit:
            max_profit = potential_profit

    return f"{max_profit:.2f}"


print(get_max_profit([5, 6], 50))
print(get_max_profit([8, 2, 5, 10], 20))
print(get_max_profit([4, 5, 3, 6], 20))
print(get_max_profit([54.40, 51.22, 53.99, 50.28, 53.01, 52.84], 200))
print(get_max_profit([15.38, 15.01, 14.99, 14.62, 14.28], 80))
print(get_max_profit([121.45, 126.82, 122.91, 124.65, 128.83, 128.83, 127.33], 1230.25))
