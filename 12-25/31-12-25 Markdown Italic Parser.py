"""
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
"""

def parse_italics(markdown: str) -> str:
    markers: set[str] = {"_", "*"}
    md_list: list[str] = markdown.split()
    parsed_list: list[str] = []

    for marker in markers:
        if marker in md_list:
            return markdown

    for item in md_list:

        if item[0] in markers and item[-1] in markers:
            parsed_list.append(f"<i>{item[1:-1]}</i>")
        elif item[-1] in markers:
            parsed_list.append(f"{item[:-1]}</i>")
        elif item[0] in markers:
            parsed_list.append(f"<i>{item[1:]}")
        else:
            parsed_list.append(item)

    return " ".join(parsed_list)


print(parse_italics("*This is italic*"))
print(parse_italics("_This is also italic_"))
print(parse_italics("*This is not italic *"))
print(parse_italics("_ This is also not italic_"))
print(parse_italics("The *quick* brown fox _jumps_ over the *lazy* dog."))
