"""
Longest Word
Given a sentence string, return the longest word in the sentence.

Words are separated by a single space.
Only letters (a-z, case-insensitive) count toward the word's length.
If there are multiple words with the same length, return the first one that appears.
Return the word as it appears in the given string, with punctuation removed.

1. longest_word("The quick red fox") should return "quick".
2. longest_word("Hello coding challenge.") should return "challenge".
3. longest_word("Do Try This At Home.") should return "This".
4. longest_word("This sentence... has commas, ellipses, and an exlamation point!") should return "exlamation".
5. longest_word("A tie? No way!") should return "tie".
6. longest_word("Wouldn't you like to know.") should return "Wouldnt".
"""

def longest_word(sentence: str) -> str:
    cleaned_sentence: str = ""
    longest_word_str: str = ""

    # Remove non-alphabetic characters from sentence.
    for char in sentence:
        if char.isalpha() or char == " ":
            cleaned_sentence += char

    # Find the longest word.
    for word in cleaned_sentence.split():
        if len(word) > len(longest_word_str):
            longest_word_str = word

    return longest_word_str


print(longest_word("The quick red fox"))
print(longest_word("Hello coding challenge."))
print(longest_word("Do Try This At Home."))
print(longest_word("This sentence... has commas, ellipses, and an exlamation point!"))
print(longest_word("A tie? No way!"))
print(longest_word("Wouldn't you like to know."))
