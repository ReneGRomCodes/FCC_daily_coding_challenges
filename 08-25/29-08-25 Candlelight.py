"""
Candlelight
Given an integer representing the number of candles you start with, and an integer representing how many burned candles
it takes to create a new one, return the number of candles you will have used after creating and burning as many as you
can.

For example, if given 7 candles and it takes 2 burned candles to make a new one:

Burn 7 candles to get 7 leftovers,
Recycle 6 leftovers into 3 new candles (1 leftover remains),
Burn 3 candles to get 3 more leftovers (4 total),
Recycle 4 leftovers into 2 new candles,
Burn 2 candles to get 2 leftovers,
Recycle 2 leftovers into 1 new candle,
Burn 1 candle.
You will have burned 13 total candles in the example.

1. burn_candles(7, 2) should return 13
2. burn_candles(10, 5) should return 12
3. burn_candles(20, 3) should return 29
4. burn_candles(17, 4) should return 22
5. burn_candles(2345, 3) should return 3517
"""

def burn_candles(candles: int, leftovers_needed: int) -> int:
    # First round of candle burning.
    candles_burnt = candles
    leftovers = candles

    # Successive rounds of candle burning and making.
    while leftovers >= leftovers_needed:
        new_candles = leftovers // leftovers_needed  # Make new candles from leftovers.
        leftovers = leftovers % leftovers_needed  # Collect leftovers left.
        candles_burnt += new_candles  # Burn new candles.
        leftovers += new_candles  # Add new leftovers to old ones.

    return candles_burnt


print(burn_candles(7, 2))
print(burn_candles(10, 5))
print(burn_candles(20, 3))
print(burn_candles(17, 4))
print(burn_candles(2345, 3))
