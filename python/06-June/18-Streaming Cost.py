"""
Streaming Cost
Given an array representing movies in the cart of your streaming service, and a string for your subscription tier, return
the total cost of the movies.

Each item in the cart is an object with a "format" ("HD" or "4K") and a "type" ("rent" or "buy"). Their costs are:

        "rent"	"buy"
"HD"	$3.99	$12.99
"4K"	$5.99	$19.99

Apply the following subscription tier discounts:
- "none": full price
- "basic": 10% off
- "premium": 25% off

Return the total cost rounded to two decimal places in the format "$D.CC".

1. getStreamingBill([{ format: "HD", type: "rent" }], "none") should return "$3.99".
2. getStreamingBill([{ format: "HD", type: "rent" }, { format: "HD", type: "buy" }], "premium") should return "$12.73".
3. getStreamingBill([{ format: "HD", type: "rent" }, { format: "HD", type: "rent" }, { format: "HD", type: "buy" }], "basic")
    should return "$18.87".
4. getStreamingBill([{ format: "4K", type: "buy" }, { format: "4K", type: "buy" }], "premium") should return "$29.98".
5. getStreamingBill([{ format: "HD", type: "rent" }, { format: "4K", type: "rent" }, { format: "HD", type: "buy" }, { format: "4K", type: "buy" }], "none")
    should return "$42.96".
6. getStreamingBill([{ format: "HD", type: "rent" }, { format: "4K", type: "rent" }, { format: "HD", type: "buy" }, { format: "4K", type: "buy" }, { format: "HD", type: "buy" }], "basic")
    should return "$50.36".
"""

def get_streaming_bill(cart: list[dict], subscription: str) -> str:
    sub_tiers: dict[str, float] = {
        "none": 1.0,
        "basic": 0.9,
        "premium": 0.75,
    }
    item_costs: dict[str, dict[str, float]] = {
        "HD": {"rent": 3.99, "buy": 12.99},
        "4K": {"rent": 5.99, "buy": 19.99},
    }
    total_price: float = 0

    for item in cart:
        total_price += item_costs[item["format"]][item["type"]]

    return f"${round(total_price, 2) * sub_tiers[subscription]:.2f}"


print(get_streaming_bill([{ "format": "HD", "type": "rent" }], "none"))
print(get_streaming_bill([{ "format": "HD", "type": "rent" }, { "format": "HD", "type": "buy" }], "premium"))
print(get_streaming_bill([{ "format": "HD", "type": "rent" }, { "format": "HD", "type": "rent" }, { "format": "HD", "type": "buy" }], "basic"))
print(get_streaming_bill([{ "format": "4K", "type": "buy" }, { "format": "4K", "type": "buy" }], "premium"))
print(get_streaming_bill([{ "format": "HD", "type": "rent" }, { "format": "4K", "type": "rent" }, { "format": "HD", "type": "buy" }, { "format": "4K", "type": "buy" }], "none"))
print(get_streaming_bill([{ "format": "HD", "type": "rent" }, { "format": "4K", "type": "rent" }, { "format": "HD", "type": "buy" }, { "format": "4K", "type": "buy" }, { "format": "HD", "type": "buy" }], "basic"))
