/*
Duplicate Character Count
Given two strings, return a count of characters from the second string that can be found in the first.

- Duplicate characters in the second string are counted separately.

1. duplicateCharacterCount("aloha", "hei") should return 1.
2. duplicateCharacterCount("jambo", "bonjour") should return 4.
3. duplicateCharacterCount("hello", "hola") should return 3.
4. duplicateCharacterCount("ola", "hej") should return 0.
5. duplicateCharacterCount("ciao", "konnichiwa") should return 5.
6. duplicateCharacterCount("merhaba", "xin chao") should return 2.
7. duplicateCharacterCount("hello world", "hello to everyone around the world") should return 26.
 */

function duplicateCharacterCount(str1, str2) {
    let counter = 0;

    for (let i = 0; i < str2.length; i++) {
        if (str1.includes(str2[i])) {
            counter++;
        }
    }

    return counter;
}


console.log(duplicateCharacterCount("aloha", "hei"));
console.log(duplicateCharacterCount("jambo", "bonjour"));
console.log(duplicateCharacterCount("hello", "hola"));
console.log(duplicateCharacterCount("ola", "hej"));
console.log(duplicateCharacterCount("ciao", "konnichiwa"));
console.log(duplicateCharacterCount("merhaba", "xin chao"));
console.log(duplicateCharacterCount("hello world", "hello to everyone around the world"));
