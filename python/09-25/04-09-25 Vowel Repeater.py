"""
Vowel Repeater
Given a string, return a new version of the string where each vowel is duplicated one more time than the previous vowel
you encountered. For instance, the first vowel in the sentence should remain unchanged. The second vowel should appear
twice in a row. The third vowel should appear three times in a row, and so on.

The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
The original vowel should keeps its case.
Repeated vowels should be lowercase.
All non-vowel characters should keep their original case.

1. repeat_vowels("hello world") should return "helloo wooorld".
2. repeat_vowels("freeCodeCamp") should return "freeeCooodeeeeCaaaaamp".
3. repeat_vowels("AEIOU") should return "AEeIiiOoooUuuuu".
4. repeat_vowels("I like eating ice cream in Iceland") should return "I liikeee eeeeaaaaatiiiiiing iiiiiiiceeeeeeee
    creeeeeeeeeaaaaaaaaaam iiiiiiiiiiin Iiiiiiiiiiiiceeeeeeeeeeeeelaaaaaaaaaaaaaand".
"""

def repeat_vowels(s: str) -> str:
    vowels: set[str] = {"a", "e", "i", "o", "u"}
    vowel_repeat_counter: int = 0
    new_s: list[str] = []

    for char in s:
        if char.lower() in vowels:
            new_s.append(char + char.lower() * vowel_repeat_counter)
            vowel_repeat_counter += 1
        else:
            new_s.append(char)

    return "".join(new_s)


print(repeat_vowels("hello world"))
print(repeat_vowels("freeCodeCamp"))
print(repeat_vowels("AEIOU"))
print(repeat_vowels("I like eating ice cream in Iceland"))
