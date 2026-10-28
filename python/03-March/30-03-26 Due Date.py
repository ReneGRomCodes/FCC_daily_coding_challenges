"""
Due Date
Given a date string, return the date 9 months in the future.

- The given and return strings have the format "YYYY-MM-DD".
- If the month nine months into the future doesn't contain the original day number, return the last day of that month.

1. get_due_date("2025-03-30") should return "2025-12-30".
2. get_due_date("2025-04-27") should return "2026-01-27".
3. get_due_date("2025-05-29") should return "2026-02-28".
4. get_due_date("2026-06-30") should return "2027-03-30".
5. get_due_date("2026-10-11") should return "2027-07-11".
"""

def get_due_date(date_str: str) -> str:
    month_lengths: dict[int, set[int]] = {
        30: {4, 6, 9, 11},  # April, June, September, November.
        31: {1, 3, 5, 7, 8, 10, 12},  # Jan, Mar, May, Jul, Aug, Oct, Dec.
        28: {2}  # No leap year involved here.
    }

    # Create list of ints [year, month, day].
    date_list: list[int] = [int(x) for x in date_str.split("-")]

    date_list[1] += 9

    if date_list[1] > 12:
        date_list[0] += 1
        date_list[1] -= 12

    for k, v in month_lengths.items():
        if date_list[1] in v and date_list[2] > k:
            date_list[2] = k

    return f"{date_list[0]}-{date_list[1]:02d}-{date_list[2]:02d}"


print(get_due_date("2025-03-30"))
print(get_due_date("2025-04-27"))
print(get_due_date("2025-05-29"))
print(get_due_date("2026-06-30"))
print(get_due_date("2026-10-11"))
