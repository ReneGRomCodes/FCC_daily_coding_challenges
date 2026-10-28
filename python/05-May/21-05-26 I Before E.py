"""
I Before E
Given a word or sentence, return a corrected version where every word follows the "I before E except after C" rule.

- If a word contains "ei" not preceded by "c", replace it with "ie".
- If a word contains "ie" preceded by "c", replace it with "ei".
- All other words are left unchanged.

1. i_before_e("beleive") should return "believe".
2. i_before_e("recieve") should return "receive".
3. i_before_e("we recieved a breif") should return "we received a brief".
4. i_before_e("she beleived the friendly niece could percieve the greif")
    should return "she believed the friendly niece could perceive the grief".
5. i_before_e("we recieved relief after the theif gave us a breif piece of feirce deceit")
    should return "we received relief after the thief gave us a brief piece of fierce deceit".
"""


def i_before_e(sentence: str) -> str:
    index: int = 0
    corrected_sentence: str = ""

    while index < len(sentence):
        char = sentence[index]
        following_chars = sentence[index + 1:index + 3]
        next_char = sentence[index + 1:index + 2]

        if char.lower() == "c" and following_chars.lower() == "ie":
            is_upper = following_chars.isupper()
            corrected_sentence += char + ("EI" if is_upper else "ei")
            index += 3  # Skip 'c', 'i', and 'e'.
            continue

        elif (char + next_char).lower() == "ei":
            if index == 0 or sentence[index - 1].lower() != "c":
                is_upper = (char + next_char).isupper()
                corrected_sentence += "IE" if is_upper else "ie"
                index += 2  # Skip 'e' and 'i'.
                continue

        # Copy single character and move forward by 1 if no rules are broken.
        corrected_sentence += char
        index += 1

    return corrected_sentence


print(i_before_e("beleive"))
print(i_before_e("recieve"))
print(i_before_e("we recieved a breif"))
print(i_before_e("she beleived the friendly niece could percieve the greif"))
print(i_before_e("we recieved relief after the theif gave us a breif piece of feirce deceit"))
