"""
Coffee Order Parser
Given a string for a coffee order, identify any menu items and return a formatted order.

Use the following menu items and prices:

Item	            Price
"cold brew"	        $4.50
"oat latte"	        $5.00
"cappuccino"	    $4.75
"espresso"	        $3.00
"vanilla syrup"	    $0.75
"caramel drizzle"	$0.60
"extra shot"	    $0.50
"oat milk"	        $0.75
"cream"	            $0.75

Return a string with the matched items joined by " + ", followed by a colon and space (": "), and the total price.

For example, given "I'd like an oat latte with vanilla syrup and an extra shot please.", return "oat latte + vanilla
syrup + extra shot: $6.25"

Items should appear in the order they appear in the menu and the total price should always have two decimal places.

1. format_coffee_order("I'd like an oat latte with vanilla syrup and an extra shot please.")
    should return "oat latte + vanilla syrup + extra shot: $6.25".
2. format_coffee_order("Give me a cappuccino with caramel drizzle, vanilla syrup, and some oat milk.")
    should return "cappuccino + vanilla syrup + caramel drizzle + oat milk: $6.85".
3. format_coffee_order("Can I get a cold brew with some cream and an extra shot.")
    should return "cold brew + extra shot + cream: $5.75".
4. format_coffee_order("Just an espresso please.") should return "espresso: $3.00".
5. format_coffee_order("I'll take an oat latte with cream and an extra shot, and some vanilla syrup and caramel drizzle.")
    should return "oat latte + vanilla syrup + caramel drizzle + extra shot + cream: $7.60".
"""

def format_coffee_order(order: str) -> str:
    menu: tuple[tuple[str, float], ...] = (
        ("cold brew", 4.5),
        ("oat latte", 5.0),
        ("cappuccino", 4.75),
        ("espresso", 3.0),
        ("vanilla syrup", 0.75),
        ("caramel drizzle", 0.6),
        ("extra shot", 0.5),
        ("oat milk", 0.75),
        ("cream", 0.75)
    )
    ordered_items: list[str] = []
    final_price: float = 0.0

    for item in menu:
        name, price = item[0], item[1]

        if name in order.lower():
            ordered_items.append(name)
            final_price += price

    return f"{' + '.join(ordered_items)}: ${final_price:.2f}"


print(format_coffee_order("I'd like an oat latte with vanilla syrup and an extra shot please."))
print(format_coffee_order("Give me a cappuccino with caramel drizzle, vanilla syrup, and some oat milk."))
print(format_coffee_order("Can I get a cold brew with some cream and an extra shot."))
print(format_coffee_order("Just an espresso please."))
print(format_coffee_order("I'll take an oat latte with cream and an extra shot, and some vanilla syrup and caramel drizzle."))
