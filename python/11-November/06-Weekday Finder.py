"""
Weekday Finder
Given a string date in the format YYYY-MM-DD, return the day of the week.

Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.

1. get_weekday("2025-11-06") should return Thursday.
2. get_weekday("1999-12-31") should return Friday.
3. get_weekday("1111-11-11") should return Saturday.
4. get_weekday("2112-12-21") should return Wednesday.
5. get_weekday("2345-10-01") should return Monday.
"""

def get_weekday(date_string: str) -> str:
    """Find and return weekday for given date string using Zeller's Congruence."""
    year, month, day = map(int, date_string.split("-"))
    weekdays: list[str] = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    if month < 3:
        month += 12
        year -= 1

    yearpart: int = year % 100
    century: int = year // 100

    day_index: int = (day + (13 * (month + 1)) // 5 + yearpart + yearpart // 4 + century // 4 + 5 * century) % 7

    return weekdays[day_index]


print(get_weekday("2025-11-06"))
print(get_weekday("1999-12-31"))
print(get_weekday("1111-11-11"))
print(get_weekday("2112-12-21"))
print(get_weekday("2345-10-01"))
