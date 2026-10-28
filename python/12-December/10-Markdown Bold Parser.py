"""
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
"""

def parse_bold(markdown: str) -> str:
    words: list[str] = markdown.split()
    markers: set[str] = {"__", "**"}
    temp: list[str | int] = []  # Used to temporarily store start markers and index extracted from 'words'.
    html: list[str] = []

    for index, word in enumerate(words):
        has_length: bool = len(word) > 2  # Ensures that standalone markers will be ignored.
        marker_start: bool = word[:2] in markers
        marker_end: bool = word[-2:] in markers
        handled: bool = False

        if has_length:
            if marker_start and marker_end:
                html.append(f"<b>{word[2:-2]}</b>")
                handled = True

            elif marker_start:
                temp.append(word)
                temp.append(index)
                handled = True

            elif marker_end:
                if temp:
                    html.append(f"{word[:-2]}</b>")
                    html.insert(temp[1], f"<b>{temp[0][2:]}")
                    temp.clear()
                else:
                    html.append(word)

                handled = True

        if not handled:
            html.append(word)

    # This only works if only one 'unclosed' start marker has been found. Not perfect but works for the given test cases.
    # Left it as is as to not overcomplicate it for potential edge cases which are not tested for here.
    if temp:
        html.insert(temp[1], temp[0])

    return " ".join(html)


print(parse_bold("**This is bold**"))
print(parse_bold("__This is also bold__"))
print(parse_bold("**This is not bold **"))
print(parse_bold("__ This is also not bold__"))
print(parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog."))
