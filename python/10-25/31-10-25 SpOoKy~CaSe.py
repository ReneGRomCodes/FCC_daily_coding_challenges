"""
SpOoKy~CaSe
Given a string representing a variable name, convert it to "spooky case" using the following constraints:

Replace all underscores (_), and hyphens (-) with a tilde (~).
Capitalize the first letter of the string, and every other letter after that, ignore the tilde character when counting.
For example, given hello_world, return HeLlO~wOrLd.

1. spookify("hello_world") should return "HeLlO~wOrLd".
2. spookify("Spooky_Case") should return "SpOoKy~CaSe".
3. spookify("TRICK-or-TREAT") should return "TrIcK~oR~tReAt".
4. spookify("c_a-n_d-y_-b-o_w_l") should return "C~a~N~d~Y~~b~O~w~L".
5. spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts") should return "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS".
"""

def spookify(boo: str) -> str:
    spookified_boo: str = ""
    char_uppercase: bool = True

    for char in boo:
        if char in {"_", "-"}:
            spookified_boo += "~"
        elif char_uppercase:
            spookified_boo += char.upper()
            char_uppercase = False
        else:
            spookified_boo += char.lower()
            char_uppercase = True

    return spookified_boo


print(spookify("hello_world"))
print(spookify("Spooky_Case"))
print(spookify("TRICK-or-TREAT"))
print(spookify("c_a-n_d-y_-b-o_w_l"))
print(spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts"))
