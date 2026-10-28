"""
S P A C E J A M
Given a string, remove all spaces from the string, insert two spaces between every character, convert all alphabetical
letters to uppercase, and return the result.

Non-alphabetical characters should remain unchanged (except for spaces).

1. space_jam("freeCodeCamp") should return "F  R  E  E  C  O  D  E  C  A  M  P".
2. space_jam("   free   Code   Camp   ") should return "F  R  E  E  C  O  D  E  C  A  M  P".
3. space_jam("Hello World?!") should return "H  E  L  L  O  W  O  R  L  D  ?  !".
4. space_jam("C@t$ & D0g$") should return "C  @  T  $  &  D  0  G  $".
5. space_jam("allyourbase") should return "A  L  L  Y  O  U  R  B  A  S  E".
"""

def space_jam(s: str) -> str:
    new_s: str = ""

    for character in s.replace(" ", ""):
        new_s += character.upper() + "  "

    new_s = new_s.rstrip()

    return new_s


print(space_jam("freeCodeCamp"))
print(space_jam("   free   Code   Camp   "))
print(space_jam("Hello World?!"))
print(space_jam("C@t$ & D0g$"))
print(space_jam("allyourbase"))
