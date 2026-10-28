"""
Credit Card Validator
Given a string of digits for a credit card number, determine if it's a valid card number using the following method:

- Starting from the second-to-last digit, double every other digit moving left.
- If doubling a digit results in a number greater than 9, subtract 9.
- Sum all the digits (doubled and undoubled).
- If the total is divisible by 10, the number is valid.

1. is_valid_card("4532015112830366") should return True.
2. is_valid_card("5425233430109903") should return True.
3. is_valid_card("371449635398431") should return True.
4. is_valid_card("6011111111111117") should return True.
5. is_valid_card("4532015112830367") should return False.
6. is_valid_card("1234567890123456") should return False.
7. is_valid_card("4532015112830368") should return False.
"""

def is_valid_card(number :str) -> bool:
    reversed_n: list[int] = [int(x) for x in number[::-1]]
    total_sum: int = 0

    for i, n in enumerate(reversed_n):
        if i % 2 != 0:
            m = n * 2
            total_sum += m if m <= 9 else m - 9
        else:
            total_sum += n

    return total_sum % 10 == 0


print(is_valid_card("4532015112830366"))
print(is_valid_card("5425233430109903"))
print(is_valid_card("371449635398431"))
print(is_valid_card("6011111111111117"))
print(is_valid_card("4532015112830367"))
print(is_valid_card("1234567890123456"))
print(is_valid_card("4532015112830368"))
