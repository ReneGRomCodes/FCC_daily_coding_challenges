"""
Is It the Weekend?
Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.

The weekend starts on Saturday.
If the given date is Saturday or Sunday, return "It's the weekend!".
Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
If X is 1, use "day" (singular) instead of "days" (plural).
Make sure the calculation ignores your local timezone.

1. days_until_weekend("2025-11-14") should return "1 day until the weekend.".
2. days_until_weekend("2025-01-01") should return "3 days until the weekend.".
3. days_until_weekend("2025-12-06") should return "It's the weekend!".
4. days_until_weekend("2026-01-27") should return "4 days until the weekend.".
5. days_until_weekend("2026-09-07") should return "5 days until the weekend.".
6. days_until_weekend("2026-11-29") should return "It's the weekend!".
"""

def days_until_weekend(date_string: str) -> str:
    """Find current weekday and return days until weekend for given date string using Zeller's Congruence."""
    year, month, day = map(int, date_string.split("-"))
    weekdays: tuple[int, ...] = (
        0,  # Saturday
        0,  # Sunday
        5,  # Monday
        4,  # Tuesday
        3,  # Wednesday
        2,  # Thursday
        1   # Friday
    )

    if month < 3:
        month += 12
        year -= 1

    yearpart: int = year % 100
    century: int = year // 100

    day_index: int = (day + (13 * (month + 1)) // 5 + yearpart + yearpart // 4 + century // 4 + 5 * century) % 7

    if weekdays[day_index] == 0:
        return "It's the weekend!"
    elif weekdays[day_index] == 1:
        return f"{weekdays[day_index]} day until the weekend."
    else:
        return f"{weekdays[day_index]} days until the weekend."


print(days_until_weekend("2025-11-14"))
print(days_until_weekend("2025-01-01"))
print(days_until_weekend("2025-12-06"))
print(days_until_weekend("2026-01-27"))
print(days_until_weekend("2026-09-07"))
print(days_until_weekend("2026-11-29"))
