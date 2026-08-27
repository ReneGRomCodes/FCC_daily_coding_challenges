/*
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
 */

function burnCandles(candles, leftoversNeeded) {
    // First round of candle burning.
    let candlesBurnt = candles;
    let leftovers = candles;

    // Successive rounds of candle burning and making.
    while (leftovers >= leftoversNeeded) {
        const newCandles = Math.floor(leftovers / leftoversNeeded);  // Make new candles from leftovers.
        leftovers %= leftoversNeeded;  // Collect leftovers left.
        candlesBurnt += newCandles;  // Burn new candles.
        leftovers += newCandles;  // Add new leftovers to old ones.
    }

    return candlesBurnt;
}


console.log(burnCandles(7, 2));
console.log(burnCandles(10, 5));
console.log(burnCandles(20, 3));
console.log(burnCandles(17, 4));
console.log(burnCandles(2345, 3));
