/*
Consonant Count
Given a string and a target number, determine whether the string contains exactly the target number of consonants.

Consonants are all alphabetic characters except "a", "e", "i", "o", and "u" in any case.
Ignore digits, punctuation, spaces, and other non-letter characters when counting.

1. has_consonant_count("helloworld", 7) should return True.
2. has_consonant_count("eieio", 5) should return False.
3. has_consonant_count("freeCodeCamp Rocks!", 11) should return True.
4. has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24) should return False.
5. has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23) should return True.
 */

function hasConsonantCount(text, target) {
    let count = 0;

    for (const char of text.toLowerCase()) {
        if (/[a-z]/i.test(char) && !["a", "e", "i", "o", "u"].includes(char)) { count++ }
        if (count > target) { return false }
    }

    return count === target;
}


console.log(hasConsonantCount("helloworld", 7));
console.log(hasConsonantCount("eieio", 5));
console.log(hasConsonantCount("freeCodeCamp Rocks!", 11));
console.log(hasConsonantCount("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24));
console.log(hasConsonantCount("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23));
