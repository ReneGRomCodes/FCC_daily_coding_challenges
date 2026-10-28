/*
Nth Fibonacci Number
Given an integer n, return the nth number in the fibonacci sequence.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10
numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

1. nth_fibonacci(4) should return 2.
2. nth_fibonacci(10) should return 34.
3. nth_fibonacci(15) should return 377.
4. nth_fibonacci(40) should return 63245986.
5. nth_fibonacci(75) should return 1304969544928657.
 */

function nthFibonacci(n) {
    let [a, b] = [0, 1];

    if (n === 0) { return a }
    else if (n === 1) { return b }
    else {
        for (let _ = 2; _ < n; _++) {
            const c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}


console.log(nthFibonacci(4));
console.log(nthFibonacci(10));
console.log(nthFibonacci(15));
console.log(nthFibonacci(40));
console.log(nthFibonacci(75));
