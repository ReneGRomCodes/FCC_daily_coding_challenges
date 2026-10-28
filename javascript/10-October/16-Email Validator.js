/*
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
 */

function validate(email) {
    const emailParts = email.split("@");
    const checkChars = "._-";
    const dot = ".";
    const doubleDot = "..";

    if (emailParts.length !== 2) { return false }  // Check if email has two parts.

    for (const part of emailParts) {
        // Filter out email with empty parts.
        if (part.length === 0) { return false }
        // Filter invalid dot positions or double dots.
        if (part[0] === dot || part[part.length - 1] === dot || part.includes(doubleDot)) { return false }
        // Check local part for invalid characters.
        if (part === emailParts[0]) {
            for (const char of part) {
                if (!/[A-Za-z0-9]/.test(char) && !checkChars.includes(char)) { return false }
            }
        }
        //Check domain part for valid dot positions and ending.
        if (part === emailParts[1]) {
            if (!part.includes(dot)) { return false }

            for (const char of part.slice(-2)) {
                if (!/[A-Za-z]/.test(char)) { return false }
            }
        }
    }

    return true;
}


console.log(validate("a@b.cd"));
console.log(validate("hell.-w.rld@example.com"));
console.log(validate(".b@sh.rc"));
console.log(validate("example@test.c0"));
console.log(validate("freecodecamp.org"));
console.log(validate("develop.ment_user@c0D!NG.R.CKS"));
console.log(validate("hello.@wo.rld"));
console.log(validate("hello@world..com"));
console.log(validate("git@commit@push.io"));
