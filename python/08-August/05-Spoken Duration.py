"""
Spoken Duration
Given a number of seconds, return the duration in spoken English.

- Break the duration into hours, minutes, and seconds.
- Skip any zero values.
- Use singular or plural as appropriate ("1 hour", "2 hours").
- If present, join the last two units with "and", and the second and third to last units with a comma ("1 hour, 2 minutes
  and 3 seconds").

1. get_spoken_duration(3723) should return "1 hour, 2 minutes and 3 seconds".
2. get_spoken_duration(7295) should return "2 hours, 1 minute and 35 seconds".
3. get_spoken_duration(8521) should return "2 hours, 22 minutes and 1 second".
4. get_spoken_duration(435) should return "7 minutes and 15 seconds".
5. get_spoken_duration(14455) should return "4 hours and 55 seconds".
6. get_spoken_duration(72000) should return "20 hours".
7. get_spoken_duration(1) should return "1 second".
"""

def get_spoken_duration(seconds: int) -> str:
    time_units: dict[str, int] = {
        "hour": seconds // 3600,
        "minute": (seconds % 3600) // 60,
        "second": seconds % 60,
    }
    spoken_duration_list: list[str] = []

    for k, v in time_units.items():
        if v:
            spoken_duration_list.append(f"{time_units[k]} {k}")
        if v > 1:
            spoken_duration_list[-1] += "s"

    if len(spoken_duration_list) == 1:
        return spoken_duration_list[0]
    elif len(spoken_duration_list) == 2:
        return " and ".join(spoken_duration_list)
    else:
        return f"{', '.join(spoken_duration_list[:2])} and {spoken_duration_list[2]}"


print(get_spoken_duration(3723))
print(get_spoken_duration(7295))
print(get_spoken_duration(8521))
print(get_spoken_duration(435))
print(get_spoken_duration(14455))
print(get_spoken_duration(72000))
print(get_spoken_duration(1))
