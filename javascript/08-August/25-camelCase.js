/*
camelCase
Given a string, return its camel case version using the following rules:

Words in the string argument are separated by one or more characters from the following set: space ( ), dash (-), or
underscore (_). Treat any sequence of these as a word break.
The first word should be all lowercase.
Each subsequent word should start with an uppercase letter, with the rest of it lowercase.
All spaces and separators should be removed.

1. to_camel_case("hello world") should return "helloWorld".
2. to_camel_case("HELLO WORLD") should return "helloWorld".
3. to_camel_case("secret agent-X") should return "secretAgentX".
4. to_camel_case("FREE cODE cAMP") should return "freeCodeCamp".
5. to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk") should return
    "yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk".
 */

function toCamelCase(s) {
    const separators = " -_";
    let cleanedS = "";
    let camelCaseS = "";

    // Build 'cleaned_s' with only single whitespace separators between words from 's'.
    for (let i=0; i < s.length; i++) {
        if (separators.includes(s[i])) {
            if (i === 0 || separators.includes(s[i - 1])) {
                continue;
            } else {
                cleanedS += " ";
            }
        } else {
            cleanedS += s[i].toLowerCase();
        }
    }

    // Split 'cleaned_s' and build 'camel_case_s'.
    const cleanedSList = cleanedS.split(" ");

    for (let i=0; i < cleanedSList.length; i++) {
        if (i === 0) {
            camelCaseS += cleanedSList[i];
        } else {
            camelCaseS += cleanedSList[i].charAt(0).toUpperCase() + cleanedSList[i].slice(1);
        }
    }

    return camelCaseS;
}


console.log(toCamelCase(" hello world"));
console.log(toCamelCase("HELLO WORLD"));
console.log(toCamelCase("secret agent-X"));
console.log(toCamelCase("FREE cODE cAMP"));
console.log(toCamelCase("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk"));
