"""
Email Validator
Given a string, determine if it is a valid email address using the following constraints:

It must contain exactly one @ symbol.
The local part (before the @):
Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
Cannot start or end with a dot.
The domain part (after the @):
Must contain at least one dot.
Must end with a dot followed by at least two letters.
Neither the local or domain part can have two dots in a row.

1. validate("a@b.cd") should return True.
2. validate("hell.-w.rld@example.com") should return True.
3. validate(".b@sh.rc") should return False.
4. validate("example@test.c0") should return False.
5. validate("freecodecamp.org") should return False.
6. validate("develop.ment_user@c0D!NG.R.CKS") should return True.
7. validate("hello.@wo.rld") should return False.
8. validate("hello@world..com") should return False.
9. validate("git@commit@push.io") should return False.
"""

def validate(email: str) -> bool:
    email_parts: list[str] = email.split("@")
    check_chars: set[str] = {".", "_", "-"}
    dot: str = "."
    double_dot: str = ".."

    if len(email_parts) != 2:  # Check if email has two parts.
        return False

    for part in email_parts:
        if len(part) == 0:  # Filter out email with empty parts.
            return False

        if part[0] == dot or part[-1] == dot or double_dot in part:  # Filter invalid dot positions or double dots.
            return False

        # Check local part for invalid characters.
        if part is email_parts[0]:
            for char in part:
                if not char.isalnum() and char not in check_chars:
                    return False

        # Check domain part for valid dot positions and ending.
        if part is email_parts[1]:
            if dot not in part:
                return False

            for char in part[-2:]:
                if not char.isalpha():
                    return False

    return True


print(validate("a@b.cd"))
print(validate("hell.-w.rld@example.com"))
print(validate(".b@sh.rc"))
print(validate("example@test.c0"))
print(validate("freecodecamp.org"))
print(validate("develop.ment_user@c0D!NG.R.CKS"))
print(validate("hello.@wo.rld"))
print(validate("hello@world..com"))
print(validate("git@commit@push.io"))
