"""
Mirror Image
Given two strings, determine if the second string is a mirror image of the first.

A mirror image is formed by reversing the string and replacing each character with its mirror equivalent.

- Symmetric characters look like themselves in a mirror:
  W, T, Y, U, I, O, H, A, X, V, M, w, o, x, v, 0, 8, =, +, :, |, -, _, *, ^, !, ., and the space ( ).

- Mirrored pairs swap with each other in a mirror:
  Character	Swaps with
    [	        ]
    {	        }
    <	        >
    b	        d
    p	        q
    (	        )

If either string includes a character not in the lists above, it doesn't have mirror image that can be created from the
characters.

For example, the mirrored image of "[HOW]" is "[WOH]".

1. is_mirror_image("[HOW]", "[WOH]") should return True.
2. is_mirror_image("MOM", "MOM") should return True.
3. is_mirror_image("vow", "wov") should return True.
4. is_mirror_image("TIM", "TIM") should return False.
5. is_mirror_image("{WOW}", "}WOW{") should return False.
6. is_mirror_image("XXVII", "IIV%X") should return False.
7. is_mirror_image("><(((*>", "<*)))><") should return True.
8. is_mirror_image("WTYUIOHAXVMwoxv08=+:|-_*^!.[]{}<>bdpq()", "()pqbd<>{}[].!^*_-|:+=80vxowMVXAHOIUYTW")
    should return True.
"""

def is_mirror_image(s1: str, s2: str) -> bool:
    mirror_chars: dict[str, str] = {
        # Symmetric characters.
        "W": "W", "T": "T", "Y": "Y", "U": "U", "I": "I", "O": "O", "H": "H", "A": "A", "X": "X", "V": "V", "M": "M",
        "w": "w", "o": "o", "x": "x", "v": "v", "0": "0", "8": "8", "=": "=", "+": "+", ":": ":", "|": "|", "-": "-",
        "_": "_", "*": "*", "^": "^", "!": "!", ".": ".", " ": " ",
        # Mirrored characters.
        "[": "]", "]": "[", "{": "}", "}": "{", "<": ">", ">": "<", "b": "d", "d": "b", "p": "q", "q": "p", "(": ")", ")": "(",
    }

    try:
        mirrored_s1: str = "".join(mirror_chars[c] for c in reversed(s1))
    except KeyError:
        return False

    return mirrored_s1 == s2


print(is_mirror_image("[HOW]", "[WOH]"))
print(is_mirror_image("MOM", "MOM"))
print(is_mirror_image("vow", "wov"))
print(is_mirror_image("TIM", "TIM"))
print(is_mirror_image("{WOW}", "}WOW{"))
print(is_mirror_image("XXVII", "IIV%X"))
print(is_mirror_image("><(((*>", "<*)))><"))
print(is_mirror_image("WTYUIOHAXVMwoxv08=+:|-_*^!.[]{}<>bdpq()", "()pqbd<>{}[].!^*_-|:+=80vxowMVXAHOIUYTW"))
