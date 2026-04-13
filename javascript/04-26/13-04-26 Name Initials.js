/*
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
 */

function getInitials(name) {
    return name
        .split(" ")
        .map(n => n[0])
        .join(".") + ".";
}


console.log(getInitials("Tommy Millwood"));
console.log(getInitials("Savanna Puddlesplash"));
console.log(getInitials("Frances Cowell Conrad"));
console.log(getInitials("Dragon"));
console.log(getInitials("Dorothy Vera Clump Haverstock Norris"));
