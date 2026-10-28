/*
Sum of Divisors
Given a positive integer, return the sum of all its divisors.

A divisor is any integer that divides the number evenly (the remainder is 0).
Only count each divisor once.
For example, given 6, return 12 because the divisors of 6 are 1, 2, 3, and 6, and the sum of those is 12.

1. sum_divisors(6) should return 12.
2. sum_divisors(13) should return 14.
3. sum_divisors(28) should return 56.
4. sum_divisors(84) should return 224.
5. sum_divisors(549) should return 806.
6. sum_divisors(9348) should return 23520.
 */

function sumDivisors(n) {
    return Array.from({ length: n }, (_, i) => i + 1)
        .filter(x => n % x === 0)
        .reduce((sum, x) => sum + x, 0);
}


console.log(sumDivisors(6));
console.log(sumDivisors(13));
console.log(sumDivisors(28));
console.log(sumDivisors(84));
console.log(sumDivisors(549));
console.log(sumDivisors(9348));
