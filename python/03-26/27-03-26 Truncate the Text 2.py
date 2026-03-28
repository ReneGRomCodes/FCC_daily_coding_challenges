"""
Truncate the Text 2
Given a string, return a new string that is truncated so that the total width of the characters does not exceed 50 units.

Each character has a specific width:
Letters	                    Width
"ilI"	                    1
"fjrt"	                    2
"abcdeghkmnopqrstuvwxyzJL"	3
"ABCDEFGHKMNOPQRSTUVWXYZ"	4

The table above includes all upper and lower case letters.

Additionally:
- Spaces (" ") have a width of 2
- Periods (".") have a width of 1
- If the given string is 50 units or less, return the string as-is, otherwise
- Truncate the string and add three periods at the end ("...") so it's total width, including the three periods, is as
  close as possible to 50 units without going over.

1. truncate_text("The quick brown fox") should return "The quick brown f...".
2. truncate_text("The silky smooth sloth") should return "The silky smooth s...".
3. truncate_text("THE LOUD BRIGHT BIRD") should return "THE LOUD BRIG...".
4. truncate_text("The fast striped zebra") should return "The fast striped z...".
5. truncate_text("The big black bear") should return "The big black bear".
"""

def truncate_text(s: str) -> str:
    chars_width: dict[int, str] = {
        1: "ilI.",
        2: "fjrt ",
        3: "abcdeghkmnopqrstuvwxyzJL",
        4: "ABCDEFGHKMNOPQRSTUVWXYZ",
    }

    width_s: int = 0
    truncated_s: str = ""

    for char in s:
        for k, v in chars_width.items():
            width_s_punctuated = width_s + len("...")

            if char in v and width_s_punctuated <= 50:
                if width_s_punctuated + k <= 50:
                    width_s += k
                    truncated_s += char
                    break
                else:
                    width_s += k
                    truncated_s += "..."

    return truncated_s


print(truncate_text("The quick brown fox"))
print(truncate_text("The silky smooth sloth"))
print(truncate_text("THE LOUD BRIGHT BIRD"))
print(truncate_text("The fast striped zebra"))
print(truncate_text("The big black bear"))
