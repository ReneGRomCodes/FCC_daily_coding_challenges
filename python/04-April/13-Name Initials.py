"""
Name Initials
Given a full name as a string, return their initials.

- Names to initialize are separated by a space.
- Initials should be made uppercase.
- Initials should be separated by dots.

For example, "Tommy Millwood" returns "T.M.".

1. get_initials("Tommy Millwood") should return "T.M.".
2. get_initials("Savanna Puddlesplash") should return "S.P.".
3. get_initials("Frances Cowell Conrad") should return "F.C.C.".
4. get_initials("Dragon") should return "D.".
5. get_initials("Dorothy Vera Clump Haverstock Norris") should return "D.V.C.H.N.".
"""

def get_initials(name: str) -> str:
    return ".".join([x[0] for x in name.split(" ")]) + "."


print(get_initials("Tommy Millwood"))
print(get_initials("Savanna Puddlesplash"))
print(get_initials("Frances Cowell Conrad"))
print(get_initials("Dragon"))
print(get_initials("Dorothy Vera Clump Haverstock Norris"))
