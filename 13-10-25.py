"""
24 to 12
Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour
format of "H:MM AM" or "H:MM PM".

The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".
1. to_12("1124") should return "11:24 AM".
2. to_12("0900") should return "9:00 AM".
3. to_12("1455") should return "2:55 PM".
4. to_12("2346") should return "11:46 PM".
5. to_12("0030") should return "12:30 AM".
"""

def to_12(time: str) -> str:
    time_hours: int = int(time[:2])
    time_minutes: int = int(time[2:])

    if time_hours > 12:
        time_hours -= 12
        suffix: str = "PM"
    elif time_hours == 12:
        suffix: str = "PM"
    else:
        if time_hours == 0:
            time_hours = 12
        suffix: str = "AM"

    time_12: str = f"{time_hours}:{time_minutes:02d} {suffix}"

    return time_12


print(to_12("1124"))
print(to_12("0900"))
print(to_12("1455"))
print(to_12("2346"))
print(to_12("0030"))
