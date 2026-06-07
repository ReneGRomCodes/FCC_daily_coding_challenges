"""
Last Load
Given the number of scoops of laundry detergent you have remaining and an array of how many scoops you used in each of
the previous days, return the number of full days of detergent you have remaining.

Calculate your average daily usage from the usage history and assume that amount of usage each day going forward.

1. last_load_date(10, [2, 2, 2, 2, 2, 2, 2]) should return 5.
2. last_load_date(16, [2, 3, 0, 3, 4, 2, 1]) should return 7.
3. last_load_date(33, [5, 0, 4, 3, 3, 2]) should return 11.
4. last_load_date(50, [2, 0, 2, 9, 12, 0, 2]) should return 12.
5. last_load_date(20, [13, 9, 12, 10, 8]) should return 1.
"""

def last_load_date(scoops: int, usage: list[int]) -> int:
    daily_average = sum(usage) / len(usage)

    return int(scoops // daily_average)


print(last_load_date(10, [2, 2, 2, 2, 2, 2, 2]))
print(last_load_date(16, [2, 3, 0, 3, 4, 2, 1]))
print(last_load_date(33, [5, 0, 4, 3, 3, 2]))
print(last_load_date(50, [2, 0, 2, 9, 12, 0, 2]))
print(last_load_date(20, [13, 9, 12, 10, 8]))
