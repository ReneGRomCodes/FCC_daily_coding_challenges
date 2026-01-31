/*
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
 */

const ZODIAC_DAYS = {
    "Capricorn": [356, 19],
    "Aquarius": [20, 49],
    "Pisces": [50, 79],
    "Aries": [80, 109],
    "Taurus": [110, 140],
    "Gemini": [141, 171],
    "Cancer": [172, 203],
    "Leo": [204, 234],
    "Virgo": [235, 265],
    "Libra": [266, 295],
    "Scorpio": [296, 325],
    "Sagittarius": [326, 355]
};

const MONTH_START_DAY = {
    1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151,
    7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334
};

function getSign(dateStr) {
    const [month, day] = dateStr.slice(5).split("-").map(Number);
    const doy = MONTH_START_DAY[month] + day;

    for (const [sign, [start, end]] of Object.entries(ZODIAC_DAYS)) {
        if ((start <= end && doy >= start && doy <= end) ||
            (start > end && (doy >= start || doy <= end))) {
            return sign;
        }
    }

    throw new Error("Invalid date");
}


console.log(getSign("2026-01-31"));
console.log(getSign("2001-06-10"));
console.log(getSign("1985-09-07"));
console.log(getSign("2023-03-19"));
console.log(getSign("2045-11-05"));
console.log(getSign("1985-12-06"));
console.log(getSign("2025-12-30"));
console.log(getSign("2018-10-08"));
console.log(getSign("1958-05-04"));
