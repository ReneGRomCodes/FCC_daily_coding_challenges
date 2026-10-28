"""
Piggy Bank
Given an object representing a piggy bank, return the total value as a string formatted as "$D.CC".

The object may contain any of the following:
Coin	    Value
pennies	    $0.01
nickels	    $0.05
dimes	    $0.10
quarters	$0.25

1. piggy_bank({"pennies": 3, "nickels": 5, "dimes": 2, "quarters": 6}) should return "$1.98".
2. piggy_bank({"pennies": 1, "nickels": 1, "dimes": 1, "quarters": 1}) should return "$0.41".
3. piggy_bank({"nickels": 8, "dimes": 6, "quarters": 5}) should return "$2.25".
4. piggy_bank({}) should return "$0.00".
5. piggy_bank({"pennies": 146, "nickels": 11, "dimes": 0, "quarters": 19}) should return "$6.76".
"""

def piggy_bank(coins: dict[str, int]) -> str:
    value: float = 0

    if "pennies" in coins:
        value += coins["pennies"] * 0.01
    if "nickels" in coins:
        value += coins["nickels"] * 0.05
    if "dimes" in coins:
        value += coins["dimes"] * 0.1
    if "quarters" in coins:
        value += coins["quarters"] * 0.25

    return f"${value:.2f}"


print(piggy_bank({"pennies": 3, "nickels": 5, "dimes": 2, "quarters": 6}))
print(piggy_bank({"pennies": 1, "nickels": 1, "dimes": 1, "quarters": 1}))
print(piggy_bank({"nickels": 8, "dimes": 6, "quarters": 5}))
print(piggy_bank({}))
print(piggy_bank({"pennies": 146, "nickels": 11, "dimes": 0, "quarters": 19}))
