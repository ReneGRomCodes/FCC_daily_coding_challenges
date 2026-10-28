/*
Markdown Inline Code Parser
Given a string of Markdown that includes one or more inline code blocks, return the equivalent HTML string.

Inline code blocks in Markdown use a single backtick (`) at the start and end of the code block text.

Return the given string with all code blocks converted to HTML code tags.

For example, given the string "Use `let` to declare the variable.", return "Use <code>let</code> to declare the variable.".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with
tags included.

1. parse_inline_code("Use `let` to declare the variable.") should return "Use <code>let</code> to declare the variable.".
2. parse_inline_code("Use `let` or `const` to declare a variable.")
    should return "Use <code>let</code> or <code>const</code> to declare a variable.".
3. parse_inline_code("Run `npm install` then `npm start`.")
    should return "Run <code>npm install</code> then <code>npm start</code>.".
 */

function parseInlineCode(markdown) {
    let marker_count = 0;
    let html = "";

    for (let char of markdown) {
        if (char === "`") {
            marker_count += 1;

            if (marker_count % 2 === 0) {
                html += "</code>";
            } else {
                html += "<code>";
            }

        } else {
            html += char;
        }
    }

    return html;
}


console.log(parseInlineCode("Use `let` to declare the variable."));
console.log(parseInlineCode("Use `let` or `const` to declare a variable."));
console.log(parseInlineCode("Run `npm install` then `npm start`."));
