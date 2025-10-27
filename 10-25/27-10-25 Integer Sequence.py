"""
Integer Sequence
Given a positive integer, return a string with all of the integers from 1 up to, and including, the given number, in
numerical order.

For example, given 5, return "12345".

1. sequence(5) should return "12345".
2. sequence(10) should return "12345678910".
3. sequence(1) should return "1".
4. sequence(27) should return "123456789101112131415161718192021222324252627".
"""

def sequence(n):
    seq: str = ""

    for i in range(1, n+1):
        seq += str(i)

    return seq


print(sequence(5))
print(sequence(10))
print(sequence(1))
print(sequence(27))
