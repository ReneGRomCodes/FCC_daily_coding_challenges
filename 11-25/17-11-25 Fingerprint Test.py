"""
Fingerprint Test
Given two strings representing fingerprints, determine if they are a match using the following rules:

Each fingerprint will consist only of lowercase letters (a-z).
Two fingerprints are considered a match if:
They are the same length.
The number of differing characters does not exceed 10% of the fingerprint length.

1. is_match("helloworld", "helloworld") should return True.
2. is_match("helloworld", "helloworlds") should return False.
3. is_match("helloworld", "jelloworld") should return True.
4. is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog") should return True.
5. is_match("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog") should return True.
6. is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat") should return False.
"""

def is_match(fingerprint_a: str, fingerprint_b: str) -> bool:
    if len(fingerprint_a) != len(fingerprint_b):
        return False

    counter: int = sum(a != b for a, b in zip(fingerprint_a, fingerprint_b))
    allowed_diff: float = 0.1 * len(fingerprint_a)
    if counter > allowed_diff:
        return False

    return True


print(is_match("helloworld", "helloworld"))
print(is_match("helloworld", "helloworlds"))
print(is_match("helloworld", "jelloworld"))
print(is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog"))
print(is_match("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog"))
print(is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat"))
