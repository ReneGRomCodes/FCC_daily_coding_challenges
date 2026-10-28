/*
Unique Characters
Given a string, determine if all the characters in the string are unique.

Uppercase and lowercase letters should be considered different characters.

1. all_unique("abc") should return True.
2. all_unique("aA") should return True.
3. all_unique("QwErTy123!@") should return True.
4. all_unique("~!@#$%^&*()_+") should return True.
5. all_unique("hello") should return False.
6. all_unique("freeCodeCamp") should return False.
7. all_unique("!@#*$%^&*()aA") should return False.
 */

function allUnique(str) {
    return new Set(str).size === str.length;
}


console.log(allUnique("abc"));
console.log(allUnique("aA"));
console.log(allUnique("QwErTy123!@"));
console.log(allUnique("~!@#$%^&*()_+"));
console.log(allUnique("hello"));
console.log(allUnique("freeCodeCamp"));
console.log(allUnique("!@#*$%^&*()aA"));
