/*
Fibonacci Sequence
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. When starting with
0 and 1, the first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

Given an array containing the first two numbers of a Fibonacci sequence, and an integer representing the length of the
sequence, return an array containing the sequence of the given length.

Your function should handle sequences of any length greater than or equal to zero.
If the length is zero, return an empty array.
Note that the starting numbers are part of the sequence.

1. fibonacci_sequence([0, 1], 20)
    should return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181].
2. fibonacci_sequence([21, 32], 1) should return [21].
3. fibonacci_sequence([0, 1], 0) should return [].
4. fibonacci_sequence([10, 20], 2) should return [10, 20].
5. fibonacci_sequence([123456789, 987654321], 5) should return [123456789, 987654321, 1111111110, 2098765431, 3209876541].
 */

function fibonacciSequence(startSequence, length) {
    // Return 'shortened' start sequence if it's length exceeds 'length' argument.
    if (startSequence.length >= length) {
        return startSequence.slice(0, length);
    }

    while (startSequence.length < length) {
        startSequence.push(
            startSequence[startSequence.length - 1] +
            startSequence[startSequence.length - 2]);
    }

    return startSequence;
}


console.log(fibonacciSequence([0, 1], 20));
console.log(fibonacciSequence([21, 32], 1));
console.log(fibonacciSequence([0, 1], 0));
console.log(fibonacciSequence([10, 20], 2));
console.log(fibonacciSequence([123456789, 987654321], 5));
