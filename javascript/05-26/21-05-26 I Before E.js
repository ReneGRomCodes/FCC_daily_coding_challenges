/*
I Before E
Given a word or sentence, return a corrected version where every word follows the "I before E except after C" rule.

- If a word contains "ei" not preceded by "c", replace it with "ie".
- If a word contains "ie" preceded by "c", replace it with "ei".
- All other words are left unchanged.

1. i_before_e("beleive") should return "believe".
2. i_before_e("recieve") should return "receive".
3. i_before_e("we recieved a breif") should return "we received a brief".
4. i_before_e("she beleived the friendly niece could percieve the greif")
    should return "she believed the friendly niece could perceive the grief".
5. i_before_e("we recieved relief after the theif gave us a breif piece of feirce deceit")
    should return "we received relief after the thief gave us a brief piece of fierce deceit".
 */


function iBeforeE(sentence) {
    let i = 0;
    let correctedSentence = "";

    while (i < sentence.length) {
        const char = sentence[i];
        const followingChars = sentence.slice(i + 1, i + 3);
        const nextChar = sentence.slice(i + 1, i + 2);

        if (char.toLowerCase() === "c" && followingChars.toLowerCase() === "ie") {
            const isUpper = followingChars === followingChars.toUpperCase();
            correctedSentence += char + (isUpper ? "EI" : "ei");
            i += 3;  // Skip 'c', 'i', and 'e'.
            continue;
        }

        else if ((char + nextChar).toLowerCase() === "ei") {
            if (i === 0 || sentence[i - 1].toLowerCase() !== "c") {
                const isUpper = (char + nextChar) === (char + nextChar).toUpperCase();
                correctedSentence += isUpper ? "IE" : "ie";
                i += 2;  // Skip 'e' and 'i'.
                continue;
            }
        }

        // Copy single character and move forward by 1 if no rules are broken.
        correctedSentence += char;
        i += 1;
    }

    return correctedSentence;
}


console.log(iBeforeE("beleive"));
console.log(iBeforeE("recieve"));
console.log(iBeforeE("we recieved a breif"));
console.log(iBeforeE("she beleived the friendly niece could percieve the greif"));
console.log(iBeforeE("we recieved relief after the theif gave us a breif piece of feirce deceit"));
