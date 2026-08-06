"""
Spoken Time
Given the angles for the hour and minute hands of an analog clock in degrees (clockwise from 12), return the time in
spoken English.

Convert the minute hand angle to minutes (360° = 60 minutes), then use the following rules:
Minutes	                Spoken
0	                    "Y o'clock"
15	                    "quarter past Y"
1–29 (excluding 15)	    "X minutes past Y"
30	                    "half past Y"
45	                    "quarter to Z"
31–59 (excluding 45)	"X minutes to Z" (where X is 60 - minutes)

Where Y is the current hour and Z is the next hour, both derived from the hour hand angle (360° = 12 hours).

Note: Hand angles may not land exactly on a number, consider rounding them somehow.

1. get_spoken_time(90, 0) should return "3 o'clock".
2. get_spoken_time(160, 120) should return "20 minutes past 5".
3. get_spoken_time(255, 180) should return "half past 8".
4. get_spoken_time(67.5, 92) should return "quarter past 2".
5. get_spoken_time(200, 240) should return "20 minutes to 7".
6. get_spoken_time(322.5, 273) should return "quarter to 11".
7. get_spoken_time(117.5, 335) should return "5 minutes to 4".
"""

def get_spoken_time(hour_angle: int | float, minute_angle: int) -> str:
    hour, minute = int(hour_angle / 360 * 12), int(minute_angle / 360 * 60)
    spoken_dict: dict[str, set[int]] = {
        f"{hour} o'clock": {0},
        f"quarter past {hour}": {15},
        f"{minute} minutes past {hour}": set(range(1, 15)).union(set(range(16, 30))),
        f"half past {hour}": {30},
        f"quarter to {hour + 1}": {45},
        f"{60 - minute} minutes to {hour + 1}": set(range(31, 45)).union(set(range(46, 60))),
    }

    for k, v in spoken_dict.items():
        if minute in v:
            return k


print(get_spoken_time(90, 0))
print(get_spoken_time(160, 120))
print(get_spoken_time(255, 180))
print(get_spoken_time(67.5, 92))
print(get_spoken_time(200, 240))
print(get_spoken_time(322.5, 273))
print(get_spoken_time(117.5, 335))
