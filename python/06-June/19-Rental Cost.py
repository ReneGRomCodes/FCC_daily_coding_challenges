"""
Rental Cost
Given a rental timestamp, a return timestamp, and a rental tier, return the total cost of the rental including any late
fees.

- Given timestamps are UTC ISO strings, for example: "2026-06-18T18:30:00Z".
- The rental tier is the number of days before the rental is due back: 1, 3, or 7.
- Rentals are due back by 12:00 PM UTC or earlier on the last day of the rental period. For example, a 1-day rental checked
  out at any time on March 15 is due back by 12:00 PM UTC on March 16.
- Each day past the due date and time incurs a late fee.

Pricing is as follows:
Tier	Base cost	Late fee per day
1 day	$4.99	    $3.99
3 days	$3.99	    $2.99
7 days	$2.99	    $0.99

Return the total cost rounded to two decimal places in the format "$D.CC".

1. get_rental_cost("2026-06-18T18:30:00Z", "2026-06-19T10:30:00Z", 1) should return "$4.99".
2. get_rental_cost("2026-06-18T14:30:00Z", "2026-06-20T12:30:00Z", 1) should return "$12.97".
3. get_rental_cost("2026-06-18T10:15:00Z", "2026-06-18T19:45:00Z", 3) should return "$3.99".
4. get_rental_cost("2026-06-18T15:20:00Z", "2026-06-23T08:10:00Z", 3) should return "$9.97".
5. get_rental_cost("2026-06-18T12:00:00Z", "2026-06-25T12:00:00Z", 7) should return "$2.99".
6. get_rental_cost("2026-06-18T08:00:00Z", "2027-06-18T14:00:00Z", 7) should return "$358.40".
"""

def parse(ts: str) -> tuple[int, ...]:
    """Parse "YYYY-MM-DDTHH:MM:SSZ" manually"""
    date_part, time_part = ts[:-1].split("T")
    year, month, day = (int(x) for x in date_part.split("-"))
    hour, minute, second = (int(x) for x in time_part.split(":"))
    return year, month, day, hour, minute, second


def days_since_epoch(year: int, month: int, day: int) -> int:
    """# Convert both timestamps to a day count since an arbitrary epoch, using a simple proleptic Gregorian day-number
    formula (no imports)."""
    # Adjust so the year "starts" in March (handles leap days cleanly)
    a: int = (14 - month) // 12
    y: int = year + 4800 - a
    m: int = month + 12 * a - 3
    return day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400


def get_rental_cost(rented: str, returned: str, tier: int) -> str:
    pricing: dict[int, tuple[float, float]] = {
        1: (4.99, 3.99),
        3: (3.99, 2.99),
        7: (2.99, 0.99),
    }
    base_cost, late_fee = pricing[tier]

    r_year, r_month, r_day, r_hour, r_min, r_sec = parse(rented)
    ret_year, ret_month, ret_day, ret_hour, ret_min, ret_sec = parse(returned)

    rented_day_num = days_since_epoch(r_year, r_month, r_day)
    returned_day_num = days_since_epoch(ret_year, ret_month, ret_day)

    # Due date is `tier` days after the rental day, due by 12:00 PM.
    due_day_num: int = rented_day_num + tier
    due_hour: int = 12

    # Compare (day_num, hour, min, sec) tuples to find lateness.
    due_point: tuple[int, int, int, int] = (due_day_num, due_hour, 0, 0)
    return_point: tuple[int, int, int, int] = (returned_day_num, ret_hour, ret_min, ret_sec)

    if return_point <= due_point:
        late_days: int = 0
    else:
        # Days strictly past the due day count as late.
        # If returned later in the due day itself but past 12:00, that's still day 0 overage,
        # so we look at how many full calendar days past due_day_num, then bump by 1 if return is late at all.
        day_diff = returned_day_num - due_day_num
        if returned_day_num == due_day_num:
            # Late on the due day itself (after 12:00) -> 1 late day.
            late_days = 1
        elif (ret_hour, ret_min, ret_sec) <= (due_hour, 0, 0):
            # Returned on a later day, but at or before 12:00 -> doesn't add the partial day.
            late_days = day_diff
        else:
            late_days = day_diff + 1

    total: float = base_cost + late_days * late_fee
    return f"${total:.2f}"


print(get_rental_cost("2026-06-18T18:30:00Z", "2026-06-19T10:30:00Z", 1))
print(get_rental_cost("2026-06-18T14:30:00Z", "2026-06-20T12:30:00Z", 1))
print(get_rental_cost("2026-06-18T10:15:00Z", "2026-06-18T19:45:00Z", 3))
print(get_rental_cost("2026-06-18T15:20:00Z", "2026-06-23T08:10:00Z", 3))
print(get_rental_cost("2026-06-18T12:00:00Z", "2026-06-25T12:00:00Z", 7))
print(get_rental_cost("2026-06-18T08:00:00Z", "2027-06-18T14:00:00Z", 7))
