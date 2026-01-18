"""
Phone Number Formatter
Given a string of eleven digits, return the string as a phone number in this format: "+D (DDD) DDD-DDDD".

1. format_number("05552340182") should return "+0 (555) 234-0182".
2. format_number("15554354792") should return "+1 (555) 435-4792".
"""

def format_number(number: str) -> str:
    element_0: str = f"+{number[0]}"
    element_1: str = f"({number[1:4]})"
    element_2: str = f"{number[4:7]}-{number[7:]}"

    return f"{element_0} {element_1} {element_2}"


print(format_number("05552340182"))
print(format_number("15554354792"))
