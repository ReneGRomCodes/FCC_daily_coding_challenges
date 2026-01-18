"""
vOwElcAsE
Given a string, return a new string where all vowels are converted to uppercase and all other alphabetical characters
are converted to lowercase.

Vowels are "a", "e", "i", "o", and "u" in any case.
Non-alphabetical characters should remain unchanged.

1. vowel_case("vowelcase") should return "vOwElcAsE".
2. vowel_case("coding is fun") should return "cOdIng Is fUn".
3. vowel_case("HELLO, world!") should return "hEllO, wOrld!".
4. vowel_case("git cherry-pick") should return "gIt chErry-pIck".
5. vowel_case("HEAD~1") should return "hEAd~1".
"""

def vowel_case(s: str) -> str:
    vowels: set[str] = {"a", "e", "i", "o", "u"}
    vowel_case_s: str = ""

    for char in s:
        if char.lower() in vowels:
            vowel_case_s += char.upper()
        else:
            vowel_case_s += char.lower()

    return vowel_case_s


print(vowel_case("vowelcase"))
print(vowel_case("coding is fun"))
print(vowel_case("HELLO, world!"))
print(vowel_case("git cherry-pick"))
print(vowel_case("HEAD~1"))
