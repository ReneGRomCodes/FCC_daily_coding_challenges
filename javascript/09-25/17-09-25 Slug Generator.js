/*
Slug Generator
Given a string, return a URL-friendly version of the string using the following constraints:

All letters should be lowercase.
All characters that are not letters, numbers, or spaces should be removed.
All spaces should be replaced with the URL-encoded space code %20.
Consecutive spaces should be replaced with a single %20.
The returned string should not have leading or trailing %20.

1. generate_slug("helloWorld") should return "helloworld".
2. generate_slug("hello world!") should return "hello%20world".
3. generate_slug(" hello-world ") should return "helloworld".
4. generate_slug("hello  world") should return "hello%20world".
5. generate_slug("  ?H^3-1*1]0! W[0%R#1]D  ") should return "h3110%20w0r1d".
 */

function generateSlug(str) {
    const url = [];
    const cleanedStr = str.toLowerCase().trim();
    const spaceCode = "%20";

    for (let i = 0; i < cleanedStr.length; i++) {
        const char = cleanedStr[i];

        if (/[A-Za-z0-9]/.test(char)) {
            url.push(char);
        } else if (char === " " && cleanedStr[i - 1] !== " ") {
            url.push(spaceCode);
        }
    }

    return url.join("");
}


console.log(generateSlug("helloWorld"));
console.log(generateSlug("hello world!"));
console.log(generateSlug(" hello-world "));
console.log(generateSlug("hello  world"));
console.log(generateSlug("  ?H^3-1*1]0! W[0%R#1]D  "));
