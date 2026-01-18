"""
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
"""

def generate_slug(s: str) -> str:
    url: str = ""
    cleaned_s: str = s.lower().strip()
    space_code: str = "%20"

    for index, char in enumerate(cleaned_s):
        if char.isalpha() or char.isnumeric():
            url += char
        elif char == " " and cleaned_s[index-1] == " ":
            continue
        elif char == " ":
            url += space_code

    return url


print(generate_slug("helloWorld"))
print(generate_slug("hello world!"))
print(generate_slug(" hello-world "))
print(generate_slug("hello  world"))
print(generate_slug("  ?H^3-1*1]0! W[0%R#1]D  "))
