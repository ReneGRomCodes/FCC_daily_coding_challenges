"""
Truncate the Text
Given a string, return it as-is if it's 20 characters or shorter. If it's longer than 20 characters, truncate it to the
first 17 characters and append "..." to the end of it (so it's 20 characters total) and return the result.

1. truncate_text("Hello, world!") should return "Hello, world!".
2. truncate_text("This string should get truncated.") should return "This string shoul...".
3. truncate_text("Exactly twenty chars") should return "Exactly twenty chars".
4. truncate_text(".....................") should return "....................".
"""

def truncate_text(text: str) -> str:
    if len(text) > 20:
        return text[:17] + "..."

    return text


print(truncate_text("Hello, world!"))
print(truncate_text("This string should get truncated."))
print(truncate_text("Exactly twenty chars"))
print(truncate_text("....................."))
