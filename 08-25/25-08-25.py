"""
camelCase
Given a string, return its camel case version using the following rules:

Words in the string argument are separated by one or more characters from the following set: space ( ), dash (-), or
underscore (_). Treat any sequence of these as a word break.
The first word should be all lowercase.
Each subsequent word should start with an uppercase letter, with the rest of it lowercase.
All spaces and separators should be removed.

1. to_camel_case("hello world") should return "helloWorld".
2. to_camel_case("HELLO WORLD") should return "helloWorld".
3. to_camel_case("secret agent-X") should return "secretAgentX".
4. to_camel_case("FREE cODE cAMP") should return "freeCodeCamp".
5. to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk") should return
    "yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk".
"""

def to_camel_case(s: str) -> str:
    separators: set[str] = {" ", "-", "_"}
    cleaned_s: str = ""
    camel_case_s: str = ""

    # Build 'cleaned_s' with only single whitespace separators between words from 's'.
    for index, char in enumerate(s):
        if char in separators:
            if index == 0 or s[index-1] in separators:
                continue
            else:
                cleaned_s += " "
        else:
            cleaned_s += char.lower()

    # Split 'cleaned_s' and build 'camel_case_s'.
    for index, word in enumerate(cleaned_s.split()):
        if index == 0:
            camel_case_s += word
        else:
            camel_case_s += word[0].upper() + word[1:]

    return camel_case_s


print(to_camel_case(" hello world"))
print(to_camel_case("HELLO WORLD"))
print(to_camel_case("secret agent-X"))
print(to_camel_case("FREE cODE cAMP"))
print(to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk"))
