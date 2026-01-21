/*
3 Strikes
Given an integer between 1 and 10,000, return a count of how many numbers from 1 up to that integer whose square contains
at least one digit 3.

1. squares_with_three(1) should return 0.
2. squares_with_three(10) should return 1.
3. squares_with_three(100) should return 19.
4. squares_with_three(1000) should return 326.
5. squares_with_three(10000) should return 4531.
 */

function squaresWithThree(n) {
    return Array.from({ length: n }, (_, i) => i + 1)
        .map(i => i ** 2)
        .filter(square => square.toString().includes("3"))
        .length;
}


console.log(squaresWithThree(1));
console.log(squaresWithThree(10));
console.log(squaresWithThree(100));
console.log(squaresWithThree(1000));
console.log(squaresWithThree(10000));
