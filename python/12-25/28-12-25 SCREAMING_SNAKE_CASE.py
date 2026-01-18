"""
SCREAMING_SNAKE_CASE
Given a string representing a variable name, return the variable name converted to SCREAMING_SNAKE_CASE.

The given variable names will be written in one of the following formats:

camelCase
PascalCase
snake_case
kebab-case
In the above formats, words are separated by an underscore (_), a hyphen (-), or a new word starts with a capital letter.

To convert to SCREAMING_SNAKE_CASE:

Make all letters uppercase
Separate words with an underscore (_)

1. to_screaming_snake_case("userEmail") should return "USER_EMAIL".
2. to_screaming_snake_case("UserPassword") should return "USER_PASSWORD".
3. to_screaming_snake_case("user_id") should return "USER_ID".
4. to_screaming_snake_case("user-address") should return "USER_ADDRESS".
5. to_screaming_snake_case("username") should return "USERNAME".
"""

def to_screaming_snake_case(variable_name: str) -> str:
    separators: set[str] = {"_", "-"}
    current_word: str = ""
    words: list[str] = []

    for index, char in enumerate(variable_name):
        if char in separators or char.isupper():
            if current_word:
                words.append(current_word)
            if char in separators:
                current_word = ""
            else:
                current_word = char

        else:
            current_word += char.upper()
            if index == len(variable_name)-1:
                words.append(current_word)

    return "_".join(words)


print(to_screaming_snake_case("userEmail"))
print(to_screaming_snake_case("UserPassword"))
print(to_screaming_snake_case("user_id"))
print(to_screaming_snake_case("user-address"))
print(to_screaming_snake_case("username"))
