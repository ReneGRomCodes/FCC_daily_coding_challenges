"""
Jbelmud Text
Given a string, return a jumbled version of that string where each word is transformed using the following constraints:

The first and last letters of the words remain in place
All letters between the first and last letter are sorted alphabetically.
The input strings will contain no punctuation, and will be entirely lowercase.

1. jbelmu("hello world") should return "hello wlord".
2. jbelmu("i love jumbled text") should return "i love jbelmud text".
3. jbelmu("freecodecamp is my favorite place to learn to code") should return "faccdeeemorp is my faiortve pacle to laern to cdoe".
4. jbelmu("the quick brown fox jumps over the lazy dog") should return "the qciuk borwn fox jmpus oevr the lazy dog".
"""

def jbelmu(text: str) -> str:
    word_list: list[str] = text.split()

    for index, word in enumerate(word_list):
        if len(word) > 3:
            sort_word_center = "".join(sorted(word[1:-1]))
            word_list[index] = word[0] + sort_word_center + word[-1]

    text = " ".join(word_list)

    return text


print(jbelmu("hello world"))
print(jbelmu("i love jumbled text"))
print(jbelmu("freecodecamp is my favorite place to learn to code"))
print(jbelmu("the quick brown fox jumps over the lazy dog"))
