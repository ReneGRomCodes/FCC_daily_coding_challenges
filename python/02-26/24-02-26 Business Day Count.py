"""
Business Day Count
Given a start date and an end date, return the number of business days between the two.

Given dates are in the format "YYYY-MM-DD".
Weekdays are business days (Monday through Friday).
Weekends are not business days (Saturday and Sunday).
Include both the start and end dates when counting.

1. count_business_days("2026-02-24", "2026-02-26") should return 3.
2. count_business_days("2026-02-24", "2026-02-28") should return 4.
3. count_business_days("2026-02-21", "2026-03-01") should return 5.
4. count_business_days("2026-03-08", "2026-03-17") should return 7.
5. count_business_days("2026-02-24", "2027-02-24") should return 262.
"""
from datetime import datetime, timedelta


def count_business_days(start_date: str, end_date: str) -> int:
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()

    count = 0
    current = start

    while current <= end:
        if current.weekday() < 5:  # 0=Mon, 6=Sun.
            count += 1
        current += timedelta(days=1)

    return count


print(count_business_days("2026-02-24", "2026-02-26"))
print(count_business_days("2026-02-24", "2026-02-28"))
print(count_business_days("2026-02-21", "2026-03-01"))
print(count_business_days("2026-03-08", "2026-03-17"))
print(count_business_days("2026-02-24", "2027-02-24"))
