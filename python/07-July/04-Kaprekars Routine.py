"""
Kaprekar's Routine
Given a 4-digit number, return the number of times you need to apply Kaprekar's routine until reaching 6174.

Kaprekar's routine works as follows:

- Arrange the digits in descending order to form the largest number
- Arrange the digits in ascending order to form the smallest number (pad with leading zeros if necessary)
- Subtract the smaller from the larger
- Repeat with the new number

1. kaprekar(1234) should return 3.
2. kaprekar(2025) should return 6.
3. kaprekar(7173) should return 4.
4. kaprekar(3164) should return 7.
5. kaprekar(8082) should return 2.
"""

def get_numbers(n):
    n_ascending: list[str] = (sorted([n for n in str(n)]))
    n_descending: list[str] = sorted(n_ascending, reverse=True)
    larger_number: int = int("".join(n_descending))
    smaller_number: int = int("".join(n_ascending))

    return larger_number, smaller_number


def kaprekar(n: int) -> int:
    larger_number, smaller_number = get_numbers(n)
    kaprekars_n = 0
    counter = 0

    while kaprekars_n != 6174:
        kaprekars_n = larger_number - smaller_number

        # Avoid infinite loop. Useless for the given test cases, but I feel funky today ;)
        if kaprekars_n == 0:
            break

        # Mathematical solution to the 'padding with zeros' instruction.
        if kaprekars_n < 10:
            kaprekars_n *= 10
        elif kaprekars_n < 100:
            kaprekars_n *= 100
        elif kaprekars_n < 1000:
            kaprekars_n *= 1000

        larger_number, smaller_number = get_numbers(kaprekars_n)
        counter += 1


    return counter


print(kaprekar(1234))
print(kaprekar(2025))
print(kaprekar(7173))
print(kaprekar(3164))
print(kaprekar(8082))
