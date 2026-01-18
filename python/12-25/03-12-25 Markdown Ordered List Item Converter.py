"""
Markdown Ordered List Item Converter
Given a string representing an ordered list item in Markdown, return the equivalent HTML string.

A valid ordered list item in Markdown must:

Start with zero or more spaces, followed by
A number (1 or greater) and a period (.), followed by
At least one space, and then
The list item text.
If the string doesn't have the exact format above, return "Invalid format". Otherwise, wrap the list item text in li
tags and return the string.

For example, given "1. My item", return "<li>My item</li>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with
tags included.

1. convert_list_item("1. My item") should return "<li>My item</li>".
2. convert_list_item(" 1.  Another item") should return "<li>Another item</li>".
3. convert_list_item("1 . invalid item") should return "Invalid format".
4. convert_list_item("2. list item text") should return "<li>list item text</li>".
5. convert_list_item(". invalid again") should return "Invalid format".
6. convert_list_item("A. last invalid") should return "Invalid format".
"""

def convert_list_item(markdown: str) -> str:
    item_number, item_text = markdown.lstrip()[0:3], markdown[3:].strip()

    if not item_number[0].isnumeric() or item_number[1:] != ". ":
        return "Invalid format"

    return f"<li>{item_text}</li>"


print(convert_list_item("1. My item"))
print(convert_list_item(" 1.  Another item"))
print(convert_list_item("1 . invalid item"))
print(convert_list_item("2. list item text"))
print(convert_list_item(". invalid again"))
print(convert_list_item("A. last invalid"))
