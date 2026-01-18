"""
Unique Characters
Given a string, determine if all the characters in the string are unique.

Uppercase and lowercase letters should be considered different characters.

1. all_unique("abc") should return True.
2. all_unique("aA") should return True.
3. all_unique("QwErTy123!@") should return True.
4. all_unique("~!@#$%^&*()_+") should return True.
5. all_unique("hello") should return False.
6. all_unique("freeCodeCamp") should return False.
7. all_unique("!@#*$%^&*()aA") should return False.
"""

def all_unique(s: str) -> bool:
    if len(set(s)) == len(s):
        return True

    return False


print(all_unique("abc"))
print(all_unique("aA"))
print(all_unique("QwErTy123!@"))
print(all_unique("~!@#$%^&*()_+"))
print(all_unique("hello"))
print(all_unique("freeCodeCamp"))
print(all_unique("!@#*$%^&*()aA"))
