"""
Word Frequency
Given a paragraph, return an array of the three most frequently occurring words.

Words in the paragraph will be separated by spaces.
Ignore case in the given paragraph. For example, treat Hello and hello as the same word.
Ignore punctuation in the given paragraph. Punctuation consists of commas (,), periods (.), and exclamation points (!).
The returned array should have all lowercase words.
The returned array should be in descending order with the most frequently occurring word first.

1. get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding")
    should return ["coding", "python", "in"].
2. get_words("I like coding. I like testing. I love debugging!") should return ["i", "like", "coding"].
3. get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!")
    should return ["debug", "test", "deploy"].
"""

def get_words(paragraph: str) -> list[str]:
    words: list[str] = paragraph.split()
    words_hist: dict[str, int] = {}

    for word in words:
        word = word.strip(".,!").lower()

        if word in words_hist:
            words_hist[word] += 1
        else:
            words_hist[word] = 1

    most_frequent_words: list[str] = sorted(words_hist, key=words_hist.get, reverse=True)[:3]

    return most_frequent_words


print(get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding"))
print(get_words("I like coding. I like testing. I love debugging!"))
print(get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!"))
