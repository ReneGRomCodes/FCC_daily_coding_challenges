"""
ISBN-13 Validator
Given a string, determine if it is a valid ISBN-13 number.

A valid ISBN-13:
- Contains only digits and hyphens
- Has exactly 13 digits after removing hyphens
- Passes the following check:
    - Multiply each digit by 1 or 3, alternating (multiply the first digit by 1, the second by 3, the third by 1, and so on).
    - The sum of the results must be divisible by 10.

1. is_valid_isbn_13("9780306406157") should return True.
2. is_valid_isbn_13("97803064061570") should return False.
3. is_valid_isbn_13("978-0-13-595705-9") should return True.
4. is_valid_isbn_13("978-030-64061A-4") should return False.
5. is_valid_isbn_13("9-7-8-0-1-3-4-7-5-7-5-9-9") should return True.
"""

def is_valid_isbn_13(s: str) -> bool:
    cleaned_s: str = "".join(s.split("-"))
    checksum: int = 0

    if len(cleaned_s) != 13:
        return False

    for pos, char in enumerate(cleaned_s, start=1):
        if not char.isnumeric():
            return False
        elif pos % 2 == 0:
            checksum += int(char) * 3
        else:
            checksum += int(char)

    return checksum % 10 == 0


print(is_valid_isbn_13("9780306406157"))
print(is_valid_isbn_13("97803064061570"))
print(is_valid_isbn_13("978-0-13-595705-9"))
print(is_valid_isbn_13("978-030-64061A-4"))
print(is_valid_isbn_13("9-7-8-0-1-3-4-7-5-7-5-9-9"))
