"""
Speed Check
Given the speed you are traveling in miles per hour (MPH), and a speed limit in kilometers per hour (KPH), determine
whether you are speeding and if you will get a warning or a ticket.

1 mile equals 1.60934 kilometers.
If you are travelling less than or equal to the speed limit, return "Not Speeding".
If you are travelling 5 KPH or less over the speed limit, return "Warning".
If you are travelling more than 5 KPH over the speed limit, return "Ticket".

1. speed_check(30, 70) should return "Not Speeding".
2. speed_check(40, 60) should return "Warning".
3. speed_check(40, 65) should return "Not Speeding".
4. speed_check(60, 90) should return "Ticket".
5. speed_check(65, 100) should return "Warning".
6. speed_check(88, 40) should return "Ticket".
"""

def speed_check(speed_mph: int, speed_limit_kph: int) -> str:
    speed_kph: float = speed_mph * 1.60934
    not_speeding: bool = speed_kph <= speed_limit_kph
    warning: bool = speed_kph <= speed_limit_kph + 5

    if not_speeding:
        return "Not Speeding"
    elif warning:
        return "Warning"
    else:
        return "Ticket"


print(speed_check(30, 70))
print(speed_check(40, 60))
print(speed_check(40, 65))
print(speed_check(60, 90))
print(speed_check(65, 100))
print(speed_check(88, 40))
