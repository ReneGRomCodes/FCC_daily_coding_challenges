"""
Traveling Shopper
Given an amount of money you have, and an array of items you want to buy, determine how many of them you can afford.

The given amount will be in the format ["Amount", "Currency Code"]. For example: ["150.00", "USD"] or ["6000", "JPY"].
Each array item you want to purchase will be in the same format.
Use the following exchange rates to convert values:

Currency	1 Unit Equals
USD	        1.00 USD
EUR	        1.10 USD
GBP	        1.25 USD
JPY	        0.0070 USD
CAD	        0.75 USD
If you can afford all the items in the list, return "Buy them all!".
Otherwise, return "Buy the first X items.", where X is the number of items you can afford when purchased in the order
given.

1. buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]) should return "Buy the first 2 items.".
2. buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]) should return "Buy them all!".
3. buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]])
    should return "Buy the first 3 items.".
4. buy_items(["5000", "JPY"], [["3.00", "USD"], ["1000", "JPY"], ["5.00", "CAD"], ["2.00", "EUR"], ["4.00", "USD"], ["2000", "JPY"]])
    should return "Buy them all!".
5. buy_items(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]])
    should return "Buy the first 5 items.".
"""

def buy_items(funds: list[str], items: list[list[str]]) -> str:
    exchange_rates_usd: dict[str, float] = {
        "eur": 1.1,
        "gbp": 1.25,
        "jpy": 0.007,
        "cad": 0.75,
    }
    funds_usd: float = 0.0
    items_usd: list[float] = []
    items_usd_sum: float = 0.0
    buy_list: list[float] = []

    if funds[1] != "USD":
        funds_usd = float(funds[0]) * float(exchange_rates_usd[funds[1].lower()])
    else:
        funds_usd = float(funds[0])

    for item in items:
        price: float = float(item[0])
        currency: str = item[1].lower()

        if currency != "usd":
            price = price * exchange_rates_usd[currency]

        items_usd.append(price)

    for item in items_usd:
        new_usd_sum = items_usd_sum + item

        if new_usd_sum <= funds_usd:
            items_usd_sum = new_usd_sum
            buy_list.append(item)
        else:
            break

    if len(buy_list) == len(items_usd):
        return "Buy them all!"
    else:
        return f"Buy the first {len(buy_list)} items."


print(buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]))
print(buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]))
print(buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]))
print(buy_items(["5000", "JPY"], [["3.00", "USD"], ["1000", "JPY"], ["5.00", "CAD"], ["2.00", "EUR"], ["4.00", "USD"], ["2000", "JPY"]]))
print(buy_items(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]]))
