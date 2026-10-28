"""
ISBN-10 Validator
Given a string, determine if it's a valid ISBN-10.

An ISBN-10 consists of hyphens ("-") and 10 other characters. After removing the hyphens ("-"):
- The first 9 characters must be digits, and
- The final character may be a digit or the letter "X", which represents the number 10.

To validate it:
- Multiply each digit (or value) by its position (multiply the first digit by 1, the second by 2, and so on).
- Add all the results together.
- If the total is divisible by 11, it's valid.

1. is_valid_isbn10("0-306-40615-2") should return True.
2. is_valid_isbn10("0-306-40615-1") should return False.
3. is_valid_isbn10("0-8044-2957-X") should return True.
4. is_valid_isbn10("X-306-40615-2") should return False.
5. is_valid_isbn10("0-6822-2589-4") should return True.
"""

def is_valid_isbn10(s: str) -> bool:
    digits: str = "0123456789"
    cleaned_s: str = "".join(s.split("-"))
    digit_sum: int = 0

    if len(cleaned_s) != 10:
        return False

    for n, char in enumerate(cleaned_s, start=1):
        if char == "X" and n != 10:  # 'X' is only allowed in last position.
            return False

        else:
            if char in digits:
                digit_sum += int(char) * n
            elif char == "X":
                digit_sum += 10 * n  # 'X' has value of 10 when in last position.
            else:
                return False

    return digit_sum % 11 == 0


print(is_valid_isbn10("0-306-40615-2"))
print(is_valid_isbn10("0-306-40615-1"))
print(is_valid_isbn10("0-8044-2957-X"))
print(is_valid_isbn10("X-306-40615-2"))
print(is_valid_isbn10("0-6822-2589-4"))
