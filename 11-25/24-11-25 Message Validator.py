"""
Message Validator
Given a message string and a validation string, determine if the message is valid.

A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
Letters are case-insensitive.
Words in the message are separated by single spaces.

1. is_valid_message("hello world", "hw") should return True.
2. is_valid_message("ALL CAPITAL LETTERS", "acl") should return True.
3. is_valid_message("Coding challenge are boring.", "cca") should return False.
4. is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD") should return True.
5. is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT") should return False.
"""

def is_valid_message(message: str, validation: str) -> bool:
    starting_letters: str = "".join([x[0] for x in message.lower().split()])

    return starting_letters == validation.lower()


print(is_valid_message("hello world", "hw"))
print(is_valid_message("ALL CAPITAL LETTERS", "acl"))
print(is_valid_message("Coding challenge are boring.", "cca"))
print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD"))
print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT"))
