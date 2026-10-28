"""
Space Week Day 6: Moon Phase
For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the
moon for that day using the following rules:

Use a simplified lunar cycle of 28 days, divided into four equal phases:

"New": days 1 - 7
"Waxing": days 8 - 14
"Full": days 15 - 21
"Waning": days 22 - 28
After day 28, the cycle repeats with day 1, a new moon.

Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
You will not be given any dates before the reference date.
Return the correct phase as a string.

1. moon_phase("2000-01-12") should return "New".
2. moon_phase("2000-01-13") should return "Waxing".
3. moon_phase("2014-10-15") should return "Full".
4. moon_phase("2012-10-21") should return "Waning".
5. moon_phase("2022-12-14") should return "New".
"""

def moon_phase(date_string: str) -> str:
    year, month, day = map(int, date_string.split("-"))

    # Days in each month.
    month_lengths: list[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Count total days for full years since 2000.
    days: int = 0
    for y in range(2000, year):
        days += 365
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            days += 1  # leap day.

    # Count days for months in current year.
    for m in range(1, month):
        if m == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            days += 29
        else:
            days += month_lengths[m - 1]

    # Add days in current month.
    days += day

    # Reference new moon: 2000-01-06 (day 6).
    days_since_new_moon: int = days - 6

    # Determine moon phase.
    day_in_cycle: int = days_since_new_moon % 28

    if 0 <= day_in_cycle <= 6:
        return "New"
    elif 7 <= day_in_cycle <= 13:
        return "Waxing"
    elif 14 <= day_in_cycle <= 20:
        return "Full"
    else:
        return "Waning"


print(moon_phase("2000-01-12"))
print(moon_phase("2000-01-13"))
print(moon_phase("2014-10-15"))
print(moon_phase("2012-10-21"))
print(moon_phase("2022-12-14"))
