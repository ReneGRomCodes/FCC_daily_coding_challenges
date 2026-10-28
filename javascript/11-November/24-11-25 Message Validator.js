/*
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
 */

function isValidMessage(message, validator) {
    const startingLetters = message.toLowerCase().split(/\s+/).map(word => word[0]).join("");

    return startingLetters === validator.toLowerCase();
}


console.log(isValidMessage("hello world", "hw"));
console.log(isValidMessage("ALL CAPITAL LETTERS", "acl"));
console.log(isValidMessage("Coding challenge are boring.", "cca"));
console.log(isValidMessage("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD"));
console.log(isValidMessage("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT"));
