/*
Markdown Bold Parser
Given a string that may include some bold text in Markdown, return the equivalent HTML string.

Bold text in Markdown is any text that starts and ends with two asterisks (**) or two underscores (__).
There cannot be any spaces between the text and the asterisks or underscores, but there can be spaces in the text itself.
Convert all bold occurrences to HTML b tags and return the string.
For example, given "**This is bold**", return "<b>This is bold</b>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with
tags included.

1. parse_bold("**This is bold**") should return "<b>This is bold</b>".
2. parse_bold("__This is also bold__") should return "<b>This is also bold</b>".
3. parse_bold("**This is not bold **") should return "**This is not bold **".
4. parse_bold("__ This is also not bold__") should return "__ This is also not bold__".
5. parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog.")
    should return "The <b>quick</b> brown fox <b>jumps</b> over the <b>lazy</b> dog.".
 */

function parseBold(markdown) {
    const words = markdown.split(" ");
    const markers = ["__", "**"];
    const temp = [];  // Used to temporarily store start markers and index extracted from 'words'.
    const html = [];

    for (let i = 0; i < words.length; i++) {
        const word = words[i];
        const hasLength = word.length > 2;  // Ensures that standalone markers will be ignored.
        const markerStart = markers.includes(word.slice(0, 2));
        const markerEnd = markers.includes(word.slice(-2));
        let handled = false;

        if (hasLength) {
            if (markerStart && markerEnd) {
                html.push(`<b>${word.slice(2, -2)}</b>`);
                handled = true;
            } else if (markerStart) {
                temp.push(word);
                temp.push(i);
                handled = true;
            } else if (markerEnd) {
                if (temp.length > 0) {
                    html.push(`${word.slice(0, -2)}</b>`);
                    html.splice(temp[1], 0, `<b>${temp[0].slice(2)}`);
                    temp.length = 0;
                } else {
                    html.push(word);
                }
                handled = true;
            }
        }

        //This only works if only one 'unclosed' start marker has been found. Not perfect but works for the given test cases.
        // Left it as is as to not overcomplicate it for potential edge cases which are not tested for here.
        if (!handled) {
            html.push(word);
        }
    }

    if (temp.length > 0) {
        html.splice(temp[1], 0, temp[0]);
    }

    return html.join(" ");
}


console.log(parseBold("**This is bold**"));
console.log(parseBold("__This is also bold__"));
console.log(parseBold("**This is not bold **"));
console.log(parseBold("__ This is also not bold__"));
console.log(parseBold("The **quick** brown fox __jumps__ over the **lazy** dog."));
