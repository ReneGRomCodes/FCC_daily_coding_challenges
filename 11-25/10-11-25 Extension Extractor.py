"""
Extension Extractor
Given a string representing a filename, return the extension of the file.

The extension is the part of the filename that comes after the last period (.).
If the filename does not contain a period or ends with a period, return "none".
The extension should be returned as-is, preserving case.

1. get_extension("document.txt") should return "txt".
2. get_extension("README") should return "none".
3. get_extension("image.PNG") should return "PNG".
4. get_extension(".gitignore") should return "gitignore".
5. get_extension("archive.tar.gz") should return "gz".
6. get_extension("final.draft.") should return "none".
"""

def get_extension(filename: str) -> str:
    signal_char: str = "."

    if signal_char not in filename or filename[-1] == signal_char:
        return "none"

    for index, char in enumerate(filename[-1::-1]):
        if char == signal_char:
            return filename[-index:]

    return "none"


print(get_extension("document.txt"))
print(get_extension("README"))
print(get_extension("image.PNG"))
print(get_extension(".gitignore"))
print(get_extension("archive.tar.gz"))
print(get_extension("final.draft."))
