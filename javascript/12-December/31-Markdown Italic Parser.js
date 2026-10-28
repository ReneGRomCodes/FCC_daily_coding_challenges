/*
Markdown Italic Parser
Given a string that may include some italic text in Markdown, return the equivalent HTML string.

Italic text in Markdown is any text that starts and ends with a single asterisk (*) or a single underscore (_).
There cannot be any spaces between the text and the asterisk or underscore, but there can be spaces in the text itself.
Convert all italic occurrences to HTML i tags and return the string.
For example, given "*This is italic*", return "<i>This is italic</i>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with
tags included.

1. parse_italics("*This is italic*") should return "<i>This is italic</i>".
2. parse_italics("_This is also italic_") should return "<i>This is also italic</i>".
3. parse_italics("*This is not italic *") should return "*This is not italic *".
4. parse_italics("_ This is also not italic_") should return "_ This is also not italic_".
5. parse_italics("The *quick* brown fox _jumps_ over the *lazy* dog.")
    should return "The <i>quick</i> brown fox <i>jumps</i> over the <i>lazy</i> dog.".
 */

function parseItalics(markdown) {
    const markers = ["_", "*"];
    const mdList = markdown.split(" ");
    const parsedList = [];

    for (const marker of markers) {
        if (mdList.includes(marker)) { return markdown }
    }

    for (const item of mdList) {
        if (markers.includes(item[0]) && markers.includes(item.at(-1))) { parsedList.push(`<i>${item.slice(1, -1)}</i>`) }
        else if (markers.includes(item.at(-1))) { parsedList.push(`${item.slice(0, -1)}</i>`) }
        else if (markers.includes(item[0])) { parsedList.push(`<i>${item.slice(1)}`) }
        else { parsedList.push(item) }
    }

    return parsedList.join(" ");
}


console.log(parseItalics("*This is italic*"));
console.log(parseItalics("_This is also italic_"));
console.log(parseItalics("*This is not italic *"));
console.log(parseItalics("_ This is also not italic_"));
console.log(parseItalics("The *quick* brown fox _jumps_ over the *lazy* dog."));
