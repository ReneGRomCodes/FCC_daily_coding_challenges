"""
Digital Detox
Given an array of your login logs, determine whether you have met your digital detox goal.

Each log is a string in the format "YYYY-MM-DD HH:mm:ss".

You have met your digital detox goal if both of the following statements are true:

You logged in no more than once within any four-hour period.
You logged in no more than 2 times on any single day.

1. digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]) should return True.
2. digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"]) should return False.
3. digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"])
    should return True.
4. digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"])
    should return False.
5. digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00",
    "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"])
    should return True.
6. digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00",
    "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"])
    should return False.
"""

def to_minutes(time: str) -> int:
    h: int = int(time[0:2])
    m: int = int(time[3:5])

    return h * 60 + m


def digital_detox(logs: list[str]) -> bool:
    if len(logs) < 2:
        return True

    # Rule 2: no more than 2 logins per day.
    per_day: dict[str, int] = {}

    for log in logs:
        day: str = log[:10]
        per_day[day] = per_day.get(day, 0) + 1

        if per_day[day] > 2:
            return False

    # Rule 1: no more than once in any 4-hour window.
    logs: list[str] = sorted(logs)

    prev_day: str = logs[0][:10]
    prev_min: int = to_minutes(logs[0][11:])

    for log in logs[1:]:
        day: str = log[:10]
        cur_min: int = to_minutes(log[11:])

        if day == prev_day:
            if cur_min - prev_min < 240:
                return False
        else:
            # Crossed midnight → add 24h to current time.
            if (cur_min + 1440) - prev_min < 240:
                return False

        prev_day: str = day
        prev_min: int = cur_min

    return True


print(digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]))
print(digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"]))
print(digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"]))
print(digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"]))
print(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00",
                     "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]))
print(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00",
                     "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]))
