"""
P@ssw0rd Str3ngth!
Given a password string, return "weak", "medium", or "strong" based on the strength of the password.

A password is evaluated according to the following rules:

It is at least 8 characters long.
It contains both uppercase and lowercase letters.
It contains at least one number.
It contains at least one special character from this set: !, @, #, $, %, ^, &, or *.
Return "weak" if the password meets fewer than two of the rules. Return "medium" if the password meets 2 or 3 of the
rules. Return "strong" if the password meets all 4 rules.

1. check_strength("123456") should return "weak".
2. check_strength("pass!!!") should return "weak".
3. check_strength("Qwerty") should return "weak".
4. check_strength("PASSWORD") should return "weak".
5. check_strength("PASSWORD!") should return "medium".
6. check_strength("PassWord%^!") should return "medium".
7. check_strength("qwerty12345") should return "medium".
8. check_strength("S3cur3P@ssw0rd") should return "strong".
9. check_strength("C0d3&Fun!") should return "strong".
"""

def check_strength(password: str) -> str:
    length_ok: bool = False
    has_upper, has_lower, has_upper_lower = False, False, False
    has_number: bool = False
    has_special: bool = False

    if len(password) >= 8:
        length_ok = True

    for char in password:
        if not has_upper_lower:
            if not has_upper and char.isupper():
                has_upper = True
            if not has_lower and char.islower():
                has_lower = True
            if has_upper and has_lower:
                has_upper_lower = True

        if not has_number and char in "0123456789":
            has_number = True

        if not has_special and char in "!@#$%^&*":
            has_special = True

    passed_checks: int = (length_ok, has_upper_lower, has_number, has_special).count(True)

    if passed_checks < 2:
        return "weak"
    elif passed_checks < 4:
        return "medium"
    else:
        return "strong"


print(check_strength("123456"))
print(check_strength("pass!!!"))
print(check_strength("Qwerty"))
print(check_strength("PASSWORD"))
print(check_strength("PASSWORD!"))
print(check_strength("PassWord%^!"))
print(check_strength("qwerty12345"))
print(check_strength("S3cur3P@ssw0rd"))
print(check_strength("C0d3&Fun!"))
