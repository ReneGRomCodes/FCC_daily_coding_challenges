/*
Message Decoder
Given a secret message string, and an integer representing the number of letters that were used to shift the message to
encode it, return the decoded string.

A positive number means the message was shifted forward in the alphabet.
A negative number means the message was shifted backward in the alphabet.
Case matters, decoded characters should retain the case of their encoded counterparts.
Non-alphabetical characters should not get decoded.

1. decode("Xlmw mw e wigvix qiwweki.", 4) should return "This is a secret message."
2. decode("Byffi Qilfx!", 20) should return "Hello World!"
3. decode("Zqd xnt njzx?", -1) should return "Are you okay?"
4. decode("oannLxmnLjvy", 9) should return "freeCodeCamp"
 */

function decode(message, shift) {
    return [...message].map(char => {
        if (!/[a-zA-Z]/.test(char)) return char;

        const base = char <= 'Z' ? 65 : 97;
        return String.fromCharCode(
            (char.charCodeAt(0) - base - shift + 26) % 26 + base
        );
    }).join("");
}


console.log(decode("Xlmw mw e wigvix qiwweki.", 4));
console.log(decode("Byffi Qilfx!", 20));
console.log(decode("Zqd xnt njzx?", -1));
console.log(decode("oannLxmnLjvy", 9));
