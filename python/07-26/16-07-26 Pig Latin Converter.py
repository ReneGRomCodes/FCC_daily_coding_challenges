"""
Pig Latin Converter
Given a string, convert it to Pig Latin using the following rules:

- If a word begins with a vowel ("a", "e", "i", "o", or "u"), add "way" to the end. For example, "universe" converts to
  "universeway".
- If a word begins with one or more consonants, move them to the end and add "ay". For example, "hello" converts to
  "ellohay".
- Preserve the case of the first letter. For example, "Hello" converts to "Ellohay".

1. pig_latin("universe") should return "universeway".
2. pig_latin("hello") should return "ellohay".
3. pig_latin("hello universe") should return "ellohay universeway".
4. pig_latin("Hello universe") should return "Ellohay universeway".
5. pig_latin("Pig Latin is fun") should return "Igpay Atinlay isway unfay".
6. pig_latin("The quick brown fox jumped over the lazy dog")
    should return "Ethay uickqay ownbray oxfay umpedjay overway ethay azylay ogday".
"""

def pig_latin(s: str) -> str:
    vowels: set[str] = {"a", "e", "i", "o", "u"}
    pig_words = []

    for word in s.split():

        if word[0].lower() in vowels:
            pig_words.append(word + "way")

        else:
            vowel_idx = 0

            while vowel_idx < len(word) and word[vowel_idx].lower() not in vowels:
                vowel_idx += 1

            consonants = word[:vowel_idx]
            rest = word[vowel_idx:]
            new_word = rest + consonants + "ay"

            if word[0].isupper():
                pig_words.append(new_word.capitalize())
            else:
                pig_words.append(new_word.lower())

    return " ".join(pig_words)


print(pig_latin("universe"))
print(pig_latin("hello"))
print(pig_latin("hello universe"))
print(pig_latin("Hello universe"))
print(pig_latin("Pig Latin is fun"))
print(pig_latin("The quick brown fox jumped over the lazy dog"))
