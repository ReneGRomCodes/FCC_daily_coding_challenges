"""
IPv4 Validator
Given a string, determine if it is a valid IPv4 Address. A valid IPv4 address consists of four integer numbers separated
by dots (.). Each number must satisfy the following conditions:

It is between 0 and 255 inclusive.
It does not have leading zeros (e.g. 0 is allowed, 01 is not).
Only numeric characters are allowed.

1. is_valid_ipv4("192.168.1.1") should return True.
2. is_valid_ipv4("0.0.0.0") should return True.
3. is_valid_ipv4("255.01.50.111") should return False.
4. is_valid_ipv4("255.00.50.111") should return False.
5. is_valid_ipv4("256.101.50.115") should return False.
6. is_valid_ipv4("192.168.101.") should return False.
7. is_valid_ipv4("192168145213") should return False.
"""

def is_valid_ipv4(ipv4: str) -> bool:
    octets: list[str] = ipv4.split(".")

    if len(octets) != 4:  # Check correct number of octets.
        return False

    for item in octets:
        try:
            item_int: int = int(item)  # Try to cast octets to ints.
        except ValueError:
            return False

        if item_int < 0 or item_int > 255:  # Check for correct value range.
            return False
        elif len(item) > 1 and item[0] == "0":  # Check for leading zeros.
            return False

    return True


print(is_valid_ipv4("192.168.1.1"))
print(is_valid_ipv4("0.0.0.0"))
print(is_valid_ipv4("255.01.50.111"))
print(is_valid_ipv4("255.00.50.111"))
print(is_valid_ipv4("256.101.50.115"))
print(is_valid_ipv4("192.168.101."))
print(is_valid_ipv4("192168145213"))
