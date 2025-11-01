"""
Signature Validation
Given a message string, a secret key string, and a signature number, determine if the signature is valid using this
encoding method:

Letters in the message and secret key have these values:
a to z have values 1 to 26 respectively.
A to Z have values 27 to 52 respectively.
All other characters have no value.
Compute the signature by taking the sum of the message plus the sum of the secret key.
For example, given the message "foo" and the secret key "bar", the signature would be 57:

f (6) + o (15) + o (15) = 36
b (2) + a (1) + r (18) = 21
36 + 21 = 57

Check if the computed signature matches the provided signature.

1. verify("foo", "bar", 57) should return True.
2. verify("foo", "bar", 54) should return False.
3. verify("freeCodeCamp", "Rocks", 238) should return True.
4. verify("Is this valid?", "No", 210) should return False.
5. verify("Is this valid?", "Yes", 233) should return True.
6. verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514) should return True.
"""

def verify(message: str, key: str, signature: int) -> bool:
    checksum: int = 0

    for char in message + key:
        if char.isalpha() and char.isupper():
            checksum += ord(char) - 38  # Subtract offset for UPPERCASE letters when using ord() method.
        elif char.isalpha() and char.islower():
            checksum += ord(char) - 96  # Subtract offset for LOWERCASE letters when using ord() method.

    return checksum == signature


print(verify("foo", "bar", 57))
print(verify("foo", "bar", 54))
print(verify("freeCodeCamp", "Rocks", 238))
print(verify("Is this valid?", "No", 210))
print(verify("Is this valid?", "Yes", 233))
print(verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514))
