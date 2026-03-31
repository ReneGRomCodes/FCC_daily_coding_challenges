"""
Wake-Up Alarm
Given a string representing the time you set your alarm and a string representing the time you actually woke up,
determine if you woke up early, on time, or late.

Both times will be given in "HH:MM" 24-hour format.

Return:
- "early" if you woke up before your alarm time.
- "on time" if you woke up at your alarm time, or within the 10 minute snooze window after the alarm time.
- "late" if you woke up more than 10 minutes after your alarm time.

Both times are on the same day.

1. alarm_check("07:00", "06:45") should return "early".
2. alarm_check("06:30", "06:30") should return "on time".
3. alarm_check("08:10", "08:15") should return "on time".
4. alarm_check("09:30", "09:45") should return "late".
5. alarm_check("08:15", "08:25") should return "on time".
6. alarm_check("05:45", "05:56") should return "late".
7. alarm_check("04:30", "04:00") should return "early".
"""

def alarm_check(alarm_time: str, wake_time: str) -> str:
    alarm_list: list[int] = [int(x) for x in alarm_time.split(":")]
    wake_list: list[int] = [int(y) for y in wake_time.split(":")]
    alarm_total_minutes = alarm_list[0] * 60 + alarm_list[1]
    wake_total_minutes = wake_list[0] * 60 + wake_list[1]

    if wake_total_minutes < alarm_total_minutes:
        return "early"
    elif wake_total_minutes <= alarm_total_minutes + 10:
        return "on time"
    else:
        return "late"


print(alarm_check("07:00", "06:45"))
print(alarm_check("06:30", "06:30"))
print(alarm_check("08:10", "08:15"))
print(alarm_check("09:30", "09:45"))
print(alarm_check("08:15", "08:25"))
print(alarm_check("05:45", "05:56"))
print(alarm_check("04:30", "04:00"))
