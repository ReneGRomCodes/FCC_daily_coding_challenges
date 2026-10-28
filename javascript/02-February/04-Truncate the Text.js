/*
Truncate the Text
Given a string, return it as-is if it's 20 characters or shorter. If it's longer than 20 characters, truncate it to the
first 17 characters and append "..." to the end of it (so it's 20 characters total) and return the result.

1. truncate_text("Hello, world!") should return "Hello, world!".
2. truncate_text("This string should get truncated.") should return "This string shoul...".
3. truncate_text("Exactly twenty chars") should return "Exactly twenty chars".
4. truncate_text(".....................") should return "....................".
 */

function truncateText(text) {
    return text.length > 20 ? text.slice(0, 17) + "..." : text;
}

console.log(truncateText("Hello, world!"));
console.log(truncateText("This string should get truncated."));
console.log(truncateText("Exactly twenty chars"));
console.log(truncateText("....................."));
