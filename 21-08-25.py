"""
Mile Pace
Given a number of miles ran, and a time in "MM:SS" (minutes:seconds) it took to run those miles, return a string for the
average time it took to run each mile in the format "MM:SS".

Add leading zeros when needed.
1. mile_pace(3, "24:00") should return "08:00".
2. mile_pace(1, "06:45") should return "06:45".
3. mile_pace(2, "07:00") should return "03:30".
4. mile_pace(26.2, "120:35") should return "04:36".
"""

def mile_pace(miles: int | float, duration: str) -> str:
    duration_list: list[str] = duration.split(":")
    avrg_mile_pace_sec: float = (int(duration_list[0]) * 60 + int(duration_list[1])) / miles
    avrg_mile_pace: str = f"{int(avrg_mile_pace_sec / 60):02d}:{int(avrg_mile_pace_sec % 60):02d}"

    return avrg_mile_pace


print(mile_pace(3, "24:00"))
print(mile_pace(1, "06:45"))
print(mile_pace(2, "07:00"))
print(mile_pace(26.2, "120:35"))
