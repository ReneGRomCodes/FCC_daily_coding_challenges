/*
Sum of Squares
Given a positive integer up to 1,000, return the sum of all the integers squared from 1 up to the number.

1. sum_of_squares(5) should return 55.
2. sum_of_squares(10) should return 385.
3. sum_of_squares(25) should return 5525.
4. sum_of_squares(500) should return 41791750.
5. sum_of_squares(1000) should return 333833500.
 */

function sumOfSquares(n) {
    const squaredSum = [];

    for (let i = 0; i <= n; i++) {
        squaredSum.push(i**2);
    }

    return squaredSum.reduce((a, b) => a + b, 0);
}


console.log(sumOfSquares(5));
console.log(sumOfSquares(10));
console.log(sumOfSquares(25));
console.log(sumOfSquares(500));
console.log(sumOfSquares(1000));
