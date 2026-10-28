"""
Hex Validator
Given a string, determine whether it is a valid CSS hex color. A valid CSS hex color must:

Start with a #, and
be followed by either 3 or 6 hexadecimal characters.
Hexadecimal characters are numbers 0 through 9 and letters a through f (case-insensitive).

1. is_valid_hex("#123") should return True.
2. is_valid_hex("#123abc") should return True.
3. is_valid_hex("#ABCDEF") should return True.
4. is_valid_hex("#0a1B2c") should return True.
5. is_valid_hex("#12G") should return False.
6. is_valid_hex("#1234567") should return False.
7. is_valid_hex("#12 3") should return False.
8. is_valid_hex("fff") should return False.
"""

def is_valid_hex(s: str) -> bool:
    valid_chars: set[str] = {"a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

    if s[0] != "#":
        return False
    elif len(s[1:]) not in {3, 6}:
        return False

    for char in s[1:]:
        if char.lower() not in valid_chars:
            return False

    return True


print(is_valid_hex("#123"))
print(is_valid_hex("#123abc"))
print(is_valid_hex("#ABCDEF"))
print(is_valid_hex("#0a1B2c"))
print(is_valid_hex("#12G"))
print(is_valid_hex("#1234567"))
print(is_valid_hex("#12 3"))
print(is_valid_hex("fff"))
