"""
lowercase words
Given a string, return only the words that are entirely lowercase, in their original order and with a space between each
word.

1. get_lowercase_words("hello GOOD world") should return "hello world".
2. get_lowercase_words("these are all lowercase") should return "these are all lowercase".
3. get_lowercase_words("less is NoT more") should return "less is more".
4. get_lowercase_words("DonT eat pizza every OTHER day") should return "eat pizza every day".
5. get_lowercase_words("the Super quick AND snEaky brown fox Leapt anD jumped over aNd AROUND the lazy SloW dog")
    should return "the quick brown fox jumped over the lazy dog".
"""

def get_lowercase_words(s: str) -> str:
    words: list[str] = s.split(" ")
    lowercase_words: list[str] = []

    for word in words:
        if word.islower():
            lowercase_words.append(word)

    return " ".join(lowercase_words)


print(get_lowercase_words("hello GOOD world"))
print(get_lowercase_words("these are all lowercase"))
print(get_lowercase_words("less is NoT more"))
print(get_lowercase_words("DonT eat pizza every OTHER day"))
print(get_lowercase_words("the Super quick AND snEaky brown fox Leapt anD jumped over aNd AROUND the lazy SloW dog"))
