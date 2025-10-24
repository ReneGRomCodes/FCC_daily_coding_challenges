"""
Acronym Builder
Given a string containing one or more words, return an acronym of the words using the following constraints:

The acronym should consist of the first letter of each word capitalized, unless otherwise noted.
The acronym should ignore the first letter of these words unless they are the first word of the given string: a, for, an,
and, by, and of.
The acronym letters should be returned in the order they are given.
The acronym should not contain any spaces.

1. build_acronym("Search Engine Optimization") should return "SEO".
2. build_acronym("Frequently Asked Questions") should return "FAQ".
3. build_acronym("National Aeronautics and Space Administration") should return "NASA".
4. build_acronym("Federal Bureau of Investigation") should return "FBI".
5. build_acronym("For your information") should return "FYI".
6. build_acronym("By the way") should return "BTW".
7. build_acronym("An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily")
    should return "AUHWPOTIMSH".
"""

def build_acronym(s: str) -> str:
    ignore: set[str] = {"a", "for", "an", "and", "by", "of"}
    s: list[str] = s.split(" ")
    new_s: list[str] = []

    # Build new list with relevant words for acronym in uppercase.
    for index, word in enumerate(s):
        if index == 0 or word.lower() not in ignore:
            new_s.append(word.upper())

    acronym = ''.join(word[0] for word in new_s)

    return acronym


print(build_acronym("Search Engine Optimization"))
print(build_acronym("Frequently Asked Questions"))
print(build_acronym("National Aeronautics and Space Administration"))
print(build_acronym("Federal Bureau of Investigation"))
print(build_acronym("For your information"))
print(build_acronym("By the way"))
print(build_acronym("An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily"))
