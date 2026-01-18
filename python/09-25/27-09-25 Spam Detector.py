"""
Spam Detector
Given a phone number in the format "+A (BBB) CCC-DDDD", where each letter represents a digit as follows:

A represents the country code and can be any number of digits.
BBB represents the area code and will always be three digits.
CCC and DDDD represent the local number and will always be three and four digits long, respectively.
Determine if it's a spam number based on the following criteria:

The country code is greater than 2 digits long or doesn't begin with a zero (0).
The area code is greater than 900 or less than 200.
The sum of first three digits of the local number appears within last four digits of the local number.
The number has the same digit four or more times in a row (ignoring the formatting characters).

1. is_spam("+0 (200) 234-0182") should return False.
2. is_spam("+091 (555) 309-1922") should return True.
3. is_spam("+1 (555) 435-4792") should return True.
4. is_spam("+0 (955) 234-4364") should return True.
5. is_spam("+0 (155) 131-6943") should return True.
6. is_spam("+0 (555) 135-0192") should return True.
7. is_spam("+0 (555) 564-1987") should return True.
8. is_spam("+00 (555) 234-0182") should return False.
"""

def is_spam(number: str) -> bool:
    elements: list[str] = number.split()

    country_code: str = elements[0].strip("+")
    area_code: str = elements[1].strip("(").strip(")")
    local_number: list[str] = elements[2].split("-")
    full_number_string: str = "".join([country_code, area_code, local_number[0], local_number[1]])

    if len(country_code) > 2 or country_code[0] != "0":
        return True
    elif not (200 <= int(area_code) <= 900):
        return True
    elif str(sum(int(x) for x in local_number[0])) in local_number[1]:
        return True

    for i in range(10):
        if str(i) * 4 in full_number_string:
            return True

    return False


print(is_spam("+0 (200) 234-0182"))
print(is_spam("+091 (555) 309-1922"))
print(is_spam("+1 (555) 435-4792"))
print(is_spam("+0 (955) 234-4364"))
print(is_spam("+0 (155) 131-6943"))
print(is_spam("+0 (555) 135-0192"))
print(is_spam("+0 (555) 564-1987"))
print(is_spam("+00 (555) 234-0182"))
