"""
Sleep Debt
Given an array of hours slept each night leading up to today, and a target number of hours per night, return how many
hours of sleep you need tonight to eliminate your sleep debt.

- Include tonight's hours in the total time needed to catch up.
- If you've slept enough to cover tonight's target or more, return 0.

1. sleepDebt([6, 6, 6, 6, 6, 6], 8) should return 20.
2. sleepDebt([6, 7, 8, 4, 8, 6], 7) should return 10.
3. sleepDebt([10, 10, 9, 10, 9, 11], 9) should return 4.
4. sleepDebt([8, 7, 6, 7, 6, 8], 6) should return 0.
5. sleepDebt([8, 9, 10, 9, 10, 7], 7) should return 0.
"""

def sleep_debt(hours_slept: list[int], target_hours: int) -> int:
    # Include tonight's target hours in debt.
    debt: int = target_hours

    for time in hours_slept:
        night_debt: int = target_hours - time
        debt += night_debt

    return max(0, debt)


print(sleep_debt([6, 6, 6, 6, 6, 6], 8))
print(sleep_debt([6, 7, 8, 4, 8, 6], 7))
print(sleep_debt([10, 10, 9, 10, 9, 11], 9))
print(sleep_debt([8, 7, 6, 7, 6, 8], 6))
print(sleep_debt([8, 9, 10, 9, 10, 7], 7))
