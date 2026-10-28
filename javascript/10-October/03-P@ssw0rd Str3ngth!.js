/*
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
 */

function checkStrength(password) {
    let lengthOk = false;
    let [hasUpper, hasLower, hasUpperLower] = [false, false, false];
    let hasNumber = false;
    let hasSpecial = false;

    if (password.length >= 8) { lengthOk = true }

    for (const char of password) {
        if (!hasUpperLower) {
            if (!hasUpper && /[A-Z]/.test(char)) { hasUpper = true }
            if (!hasUpperLower && /[a-z]/.test(char)) { hasLower = true }
            if (hasUpper && hasLower) { hasUpperLower = true }
        }
        if (!hasNumber && "0123456789".includes(char)) { hasNumber = true }
        if (!hasSpecial && "!@#$%^&*".includes(char)) { hasSpecial = true }
    }

    const passedChecks = [lengthOk, hasUpperLower, hasNumber, hasSpecial].filter(Boolean).length;

    if (passedChecks < 2) { return "weak" }
    else if (passedChecks < 4) { return "medium" }
    else { return "strong" }
}


console.log(checkStrength("123456"));
console.log(checkStrength("pass!!!"));
console.log(checkStrength("Qwerty"));
console.log(checkStrength("PASSWORD"));
console.log(checkStrength("PASSWORD!"));
console.log(checkStrength("PassWord%^!"));
console.log(checkStrength("qwerty12345"));
console.log(checkStrength("S3cur3P@ssw0rd"));
console.log(checkStrength("C0d3&Fun!"));
