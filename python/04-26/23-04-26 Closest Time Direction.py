"""
Closest Time Direction
Given two times, determine whether you can get from the first to the second faster by moving forward or backward.

- Times are given in 24-hour format ("HH:MM")
- The clock wraps around (23:59 goes to 00:00 when moving forward, and 00:00 goes to 23:59 when moving backwards)

Return:
- "forward" if moving forward is shorter
- "backward" if moving backward is shorter
- "equal" if both directions take the same amount of time

1. get_direction("10:00", "12:00") should return "forward".
2. get_direction("11:00", "05:00") should return "backward".
3. get_direction("00:00", "12:00") should return "equal".
4. get_direction("15:45", "01:10") should return "forward".
5. get_direction("03:30", "19:50") should return "backward".
6. get_direction("06:30", "18:30") should return "equal".
"""

def get_direction(time1: str, time2: str) -> str:
    h1, m1 = map(int, time1.split(":"))
    h2, m2 = map(int, time2.split(":"))

    diff = ((h2 * 60 + m2) - (h1 * 60 + m1)) % 1440

    if diff < 720:
        return "forward"
    elif diff > 720:
        return "backward"
    else:
        return "equal"


print(get_direction("10:00", "12:00"))
print(get_direction("11:00", "05:00"))
print(get_direction("00:00", "12:00"))
print(get_direction("15:45", "01:10"))
print(get_direction("03:30", "19:50"))
print(get_direction("06:30", "18:30"))
