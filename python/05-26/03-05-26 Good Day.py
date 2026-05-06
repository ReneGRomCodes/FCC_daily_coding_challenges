"""
Good Day
Given a time string in "HH:MM" format (24-hour clock), return:

- "Good morning" for times 05:00 to 11:59
- "Good afternoon" for times 12:00 to 17:59
- "Good evening" for times 18:00 to 21:59
- "Good night" for times 22:00 to 04:59

1. getGreeting("06:30") should return "Good morning".
2. getGreeting("12:00") should return "Good afternoon".
3. getGreeting("21:59") should return "Good evening".
4. getGreeting("00:01") should return "Good night".
5. getGreeting("11:30") should return "Good morning".
"""

def get_greeting(s: str) -> str | None:
    morning_start_hrs: int = 5
    afternoon_start_hrs: int = 12
    evening_start_hrs: int = 18
    night_start_hrs: int = 22
    midnight_mins: tuple[int, int] = (0, 24 * 60)

    daytime: dict[str, tuple[int, int]] = {
        "morning": (morning_start_hrs * 60, afternoon_start_hrs * 60),
        "afternoon": (afternoon_start_hrs * 60, evening_start_hrs * 60),
        "evening": (evening_start_hrs * 60, night_start_hrs * 60),
        "night": (night_start_hrs * 60, midnight_mins[1]),
        "NIGHT": (midnight_mins[0], morning_start_hrs * 60),
    }

    s_minutes: int = int(s.split(":")[0]) * 60 + int(s.split(":")[1])

    for k, v in daytime.items():
        if v[0] <= s_minutes < v[1]:
            return f"Good {k.lower()}"

    return None


print(get_greeting("06:30"))
print(get_greeting("12:00"))
print(get_greeting("21:59"))
print(get_greeting("00:01"))
print(get_greeting("11:30"))
