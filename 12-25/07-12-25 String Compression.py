"""
String Compression
Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by
the word followed with the number of times it repeats in parentheses.

Only consecutive duplicates are compressed.
Words are separated by single spaces.
For example, given "yes yes yes please", return "yes(3) please".

1. compress_string("yes yes yes please") should return "yes(3) please".
2. compress_string("I have have have apples") should return "I have(3) apples".
3. compress_string("one one three and to the the the the") should return "one(2) three and to the(4)".
4. compress_string("route route route route route route tee tee tee tee tee tee") should return "route(6) tee(6)".
"""

def compress_string(sentence: str) -> str:
    """This solution is far from perfect. Duplicate words are counted throughout the sentence, not only if they are
    consecutive. This one is does fulfill the challenge requirements and is easy to read though."""
    counted: list[tuple[str, int]] = []
    new_sentence: str = ""

    for word in sentence.split():
        if (word, sentence.count(word)) not in counted:
            counted.append((word, sentence.count(word)))

    for count in counted:
        if count[1] > 1:
            new_sentence += f"{count[0]}({count[1]}) "
        else:
            new_sentence += f"{count[0]} "

    return new_sentence[:-1]


def compress_string_alternative(sentence: str) -> str:
    """More thorough solution to the challenge which takes non-consecutive duplicates into account."""
    words: list[str] = sentence.split()
    result: list[str] = []
    current: str = words[0]
    count: int = 1

    for word in words[1:]:
        if word == current:
            count += 1
        else:
            if count > 1:
                result.append(f"{current}({count})")
            else:
                result.append(current)
            current = word
            count = 1

    # Handle the last word/run.
    if count > 1:
        result.append(f"{current}({count})")
    else:
        result.append(current)

    return " ".join(result)


print(compress_string("yes yes yes please"))
print(compress_string("I have have have apples"))
print(compress_string("one one three and to the the the the"))
print(compress_string("route route route route route route tee tee tee tee tee tee"))
