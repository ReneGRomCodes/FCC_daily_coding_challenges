"""
Zodiac Finder
Given a date string in the format "YYYY-MM-DD", return the zodiac sign for that date using the following chart:

Date Range	                Zodiac Sign
March 21 - April 19	        "Aries"
April 20 - May 20	        "Taurus"
May 21 - June 20	        "Gemini"
June 21 - July 22	        "Cancer"
July 23 - August 22	        "Leo"
August 23 - September 22	"Virgo"
September 23 - October 22	"Libra"
October 23 - November 21	"Scorpio"
November 22 - December 21	"Sagittarius"
December 22 - January 19	"Capricorn"
January 20 - February 18	"Aquarius"
February 19 - March 20	    "Pisces"

Zodiac signs are based only on the month and day, you can ignore the year.

1. get_sign("2026-01-31") should return "Aquarius".
2. get_sign("2001-06-10") should return "Gemini".
3. get_sign("1985-09-07") should return "Virgo".
4. get_sign("2023-03-19") should return "Pisces".
5. get_sign("2045-11-05") should return "Scorpio".
6. get_sign("1985-12-06") should return "Sagittarius".
7. get_sign("2025-12-30") should return "Capricorn".
8. get_sign("2018-10-08") should return "Libra".
9. get_sign("1958-05-04") should return "Taurus".
"""

# Each value is (start_day_of_year, end_day_of_year)
ZODIAC_DAYS = {
    "Capricorn":    (356, 19),   # wraps the year
    "Aquarius":     (20, 49),
    "Pisces":       (50, 79),
    "Aries":        (80, 109),
    "Taurus":       (110, 140),
    "Gemini":       (141, 171),
    "Cancer":       (172, 203),
    "Leo":          (204, 234),
    "Virgo":        (235, 265),
    "Libra":        (266, 295),
    "Scorpio":      (296, 325),
    "Sagittarius":  (326, 355),
}


MONTH_START_DAY = {1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,10:273,11:304,12:334}


def get_sign(date_str: str) -> str:
    month, day = [int(x) for x in date_str[5:].split("-")]
    doy = MONTH_START_DAY[month] + day

    for sign, (start, end) in ZODIAC_DAYS.items():
        if start <= end and start <= doy <= end or start > end and (doy >= start or doy <= end):
            return sign

    return date_str


print(get_sign("2026-01-31"))
print(get_sign("2001-06-10"))
print(get_sign("1985-09-07"))
print(get_sign("2023-03-19"))
print(get_sign("2045-11-05"))
print(get_sign("1985-12-06"))
print(get_sign("2025-12-30"))
print(get_sign("2018-10-08"))
print(get_sign("1958-05-04"))
