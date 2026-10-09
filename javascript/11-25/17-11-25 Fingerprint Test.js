/*
Fingerprint Test
Given two strings representing fingerprints, determine if they are a match using the following rules:

Each fingerprint will consist only of lowercase letters (a-z).
Two fingerprints are considered a match if:
They are the same length.
The number of differing characters does not exceed 10% of the fingerprint length.

1. is_match("helloworld", "helloworld") should return True.
2. is_match("helloworld", "helloworlds") should return False.
3. is_match("helloworld", "jelloworld") should return True.
4. is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog") should return True.
5. is_match("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog") should return True.
6. is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat") should return False.
 */

function isMatch(fingerprintA, fingerprintB) {

    return fingerprintA;
}


console.log(isMatch("helloworld", "helloworld"));
console.log(isMatch("helloworld", "helloworlds"));
console.log(isMatch("helloworld", "jelloworld"));
console.log(isMatch("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog"));
console.log(isMatch("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog"));
console.log(isMatch("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat"));
