"""
What's My Age Again?
Given the date of someone's birthday in the format YYYY-MM-DD, return the person's age as of November 27th, 2025.

Assume all birthdays are valid dates before November 27th, 2025.
Return the age as an integer.
Be sure to account for whether the person has already had their birthday in 2025.

1. calculate_age("2000-11-20") should return 25.
2. calculate_age("2000-12-01") should return 24.
3. calculate_age("2014-10-25") should return 11.
4. calculate_age("1994-01-06") should return 31.
5. calculate_age("1994-12-14") should return 30.
"""

def calculate_age(birthday: str) -> int:
    year: int = int(birthday[0:4])
    month: int = int(birthday[5:7])
    day: int = int(birthday[8:10])

    ref_year, ref_month, ref_day = 2025, 11, 27

    age: int = ref_year - year

    # If their 2025 birthday hasn't happened yet, subtract 1
    if (month, day) > (ref_month, ref_day):
        age -= 1

    return age


print(calculate_age("2000-11-20"))
print(calculate_age("2000-12-01"))
print(calculate_age("2014-10-25"))
print(calculate_age("1994-01-06"))
print(calculate_age("1994-12-14"))
