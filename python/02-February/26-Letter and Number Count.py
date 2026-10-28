"""
Letter and Number Count
Given a string, return a message with the count of how many letters and numbers it contains.

Letters are A-Z and a-z.
Numbers are 0-9.
Ignore all other characters.

Return "The string has X letters and Y numbers.", where "X" is the count of letters and "Y" is the count of numbers. If
either count is 1, use the singular form for that item. E.g: "1 letter" instead of "1 letters" and "1 number" instead
of "1 numbers".

1. countLettersAndNumbers("helloworld123") should return "The string has 10 letters and 3 numbers.".
2. countLettersAndNumbers("Catch 22") should return "The string has 5 letters and 2 numbers.".
3. countLettersAndNumbers("A1!") should return "The string has 1 letter and 1 number.".
4. countLettersAndNumbers("12345") should return "The string has 0 letters and 5 numbers.".
5. countLettersAndNumbers("password") should return "The string has 8 letters and 0 numbers.".
"""

def count_letters_and_numbers(s: str) -> str:
    letters_n: int = 0
    numbers_n: int = 0

    for char in s:
        if char.isalpha():
            letters_n += 1
        elif char.isnumeric():
            numbers_n += 1

    # Build f-strings and get the grammar straight.
    letters_s: str = f"{letters_n} letter"
    numbers_s: str = f"{numbers_n} number"

    if letters_n > 1 or letters_n == 0:
        letters_s += "s"
    if numbers_n > 1 or numbers_n == 0:
        numbers_s += "s"

    return f"The string has {letters_s} and {numbers_s}."


print(count_letters_and_numbers("helloworld123"))
print(count_letters_and_numbers("Catch 22"))
print(count_letters_and_numbers("A1!"))
print(count_letters_and_numbers("12345"))
print(count_letters_and_numbers("password"))
