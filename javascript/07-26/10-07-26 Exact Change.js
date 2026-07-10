/*
Exact Change
Given an integer amount in cents, return the number of distinct ways to make exact change using pennies (1 cent),
nickels (5 cents), dimes (10 cents), and quarters (25 cents).

1. exact_change(3) should return 1.
2. exact_change(9) should return 2.
3. exact_change(17) should return 6.
4. exact_change(39) should return 24.
5. exact_change(61) should return 73.
6. exact_change(99) should return 213.
 */

function exactChange(amount) {
    const ways = new Array(amount + 1).fill(0);
    ways[0] = 1;
    const coins = [1, 5, 10, 25];

    for (const coin of coins) {
        for (let currentAmount = coin; currentAmount <= amount; currentAmount++) {
            ways[currentAmount] += ways[currentAmount - coin];
        }
    }

    return ways[amount];
}


console.log(exactChange(3));
console.log(exactChange(9));
console.log(exactChange(17));
console.log(exactChange(39));
console.log(exactChange(61));
console.log(exactChange(99));
