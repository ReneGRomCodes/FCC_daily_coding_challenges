"""
Vowel Balance
Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels
in the second half.

The string can contain any characters.
The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
If there's an odd number of characters in the string, ignore the center character.

1. is_balanced("racecar") should return True.
2. is_balanced("Lorem Ipsum") should return True.
3. is_balanced("Kitty Ipsum") should return False.
4. is_balanced("string") should return False.
5. is_balanced(" ") should return True.
6. is_balanced("abcdefghijklmnopqrstuvwxyz") should return False.
7. is_balanced("123A#b!E&*456-o.U") should return True.
"""

VOWELS: set[str] = {"a", "e", "i", "o", "u"}

def is_balanced(s) -> bool:
    s: str = s.lower()
    s_len: int = len(s)
    is_s_list_odd: bool = s_len % 2 != 0

    vowel_counter_a: int = 0
    vowel_counter_b: int = 0

    if is_s_list_odd:
        center_index: int = int((s_len - 1) / 2)
        s = s[:center_index] + s[center_index+1:]  # 'Ignoring' the center index by removing it for odd length 's'.
    else:
        center_index: int = int(s_len / 2)

    for vowel in VOWELS:
        vowel_counter_a += s[:center_index].count(vowel)
        vowel_counter_b += s[center_index:].count(vowel)

    return vowel_counter_a == vowel_counter_b


print(is_balanced("racecar"))
print(is_balanced("Lorem Ipsum"))
print(is_balanced("Kitty Ipsum"))
print(is_balanced("string"))
print(is_balanced(" "))
print(is_balanced("abcdefghijklmnopqrstuvwxyz"))
print(is_balanced("123A#b!E&*456-o.U"))
