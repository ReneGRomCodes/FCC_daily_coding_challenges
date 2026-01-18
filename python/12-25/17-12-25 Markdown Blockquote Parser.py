"""
Markdown Blockquote Parser
Given a string that includes a blockquote in Markdown, return the equivalent HTML string.

A blockquote in Markdown is any line that:

Starts with zero or more spaces
Followed by a greater-than sign (>)
Then, one or more spaces
And finally, the blockquote text.
Return the blockquote text surrounded by opening and closing HTML blockquote tags.

For example, given "> This is a quote", return <blockquote>This is a quote</blockquote>.

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with
tags included.

1. parse_blockquote("> This is a quote") should return "<blockquote>This is a quote</blockquote>".
2. parse_blockquote(" > This is also a quote") should return "<blockquote>This is also a quote</blockquote>".
3. parse_blockquote("  >    So  Is  This") should return "<blockquote>So  Is  This</blockquote>".
"""

def parse_blockquote(markdown: str) -> str:
    return f"<blockquote>{markdown.lstrip(' >')}</blockquote>"


print(parse_blockquote("> This is a quote"))
print(parse_blockquote(" > This is also a quote"))
print(parse_blockquote("  >    So  Is  This"))
