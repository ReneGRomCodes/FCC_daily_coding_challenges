"""
Summer Solstice
Today is the summer solstice, the longest day of the year in the Northern Hemisphere and the shortest in the Southern.
Given a latitude, return a string representing daytime and nighttime hours.

- The latitude will be between 90 (north pole) and -90 (south pole), inclusive
- The number of daytime hours = 12 + (latitude / 90) * 12
- Round the daytime hours to the nearest even number

Return a 24-character string using "☀️" for daytime hours and "🌑" for nighttime hours, where:

- Each character represents one hour, starting at midnight (hour 0)
- Sunrise and sunset fall symmetrically around noon

For example, a latitude of 0 (the equator) has 12 hours of daylight, so sunrise is at 6:00 AM and sunset is at 6:00 PM.
Return: "🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑".

1. get_daytime_hours(0) should return "🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑".
2. get_daytime_hours(90) should return "☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️".
3. get_daytime_hours(-90) should return "🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑🌑".
4. get_daytime_hours(-33) should return "🌑🌑🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑🌑🌑".
5. get_daytime_hours(66.5) should return "🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑".
6. get_daytime_hours(40) should return "🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑".
7. get_daytime_hours(-50) should return "🌑🌑🌑🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑🌑🌑🌑".
"""

def get_daytime_hours(latitude: int | float) -> str:
    daytime_symbol, nighttime_symbol = "☀️", "🌑"
    daytime_hours_n: int = round((12 + (latitude / 90) * 12) / 2) * 2  # Rounded to nearest even number.
    nighttime_hours_n: int = 24 - daytime_hours_n

    return nighttime_symbol * int(nighttime_hours_n / 2) + daytime_symbol * daytime_hours_n + nighttime_symbol * int(nighttime_hours_n / 2)


print(get_daytime_hours(0))
print(get_daytime_hours(90))
print(get_daytime_hours(-90))
print(get_daytime_hours(-33))
print(get_daytime_hours(66.5))
print(get_daytime_hours(40))
print(get_daytime_hours(-50))
