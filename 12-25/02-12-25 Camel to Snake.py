"""
Camel to Snake
Given a string in camel case, return the snake case version of the string using the following rules:

The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
Every uppercase letter in the camel case string starts a new word.
Convert all letters to lowercase.
Separate words with an underscore (_).

1. to_snake("helloWorld") should return "hello_world".
2. to_snake("myVariableName") should return "my_variable_name".
3. to_snake("freecodecampDailyChallenges") should return "freecodecamp_daily_challenges".
"""

def to_snake(camel: str) -> str:
    snake: str = ""

    for char in camel:
        if not char.isupper():
            snake += char
            continue

        snake += "_" + char.lower()

    return snake


print(to_snake("helloWorld"))
print(to_snake("myVariableName"))
print(to_snake("freecodecampDailyChallenges"))
