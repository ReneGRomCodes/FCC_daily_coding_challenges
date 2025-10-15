"""
Fibonacci Sequence
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. When starting with
0 and 1, the first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

Given an array containing the first two numbers of a Fibonacci sequence, and an integer representing the length of the
sequence, return an array containing the sequence of the given length.

Your function should handle sequences of any length greater than or equal to zero.
If the length is zero, return an empty array.
Note that the starting numbers are part of the sequence.

1. fibonacci_sequence([0, 1], 20) should return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181].
2. fibonacci_sequence([21, 32], 1) should return [21].
3. fibonacci_sequence([0, 1], 0) should return [].
4. fibonacci_sequence([10, 20], 2) should return [10, 20].
5. fibonacci_sequence([123456789, 987654321], 5) should return [123456789, 987654321, 1111111110, 2098765431, 3209876541].
"""

def fibonacci_sequence(start_sequence: list[int], length: int) -> list[int]:
    # Return 'shortened' start sequence if it's length exceeds 'length' argument.
    if len(start_sequence) >= length:
        return start_sequence[:length]

    while len(start_sequence) < length:
        start_sequence.append(start_sequence[-1] + start_sequence[-2])

    return start_sequence


print(fibonacci_sequence([0, 1], 20))
print(fibonacci_sequence([21, 32], 1))
print(fibonacci_sequence([0, 1], 0))
print(fibonacci_sequence([10, 20], 2))
print(fibonacci_sequence([123456789, 987654321], 5))
