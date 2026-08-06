/*
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
 */

function getSpokenTime(hourAngle, minuteAngle) {
    const hour = Math.floor(hourAngle / 360 * 12);
    const minute = Math.floor(minuteAngle / 360 * 60);

    const specialCases = {
        0: `${hour} o'clock`,
        15: `quarter past ${hour}`,
        30: `half past ${hour}`,
        45: `quarter to ${hour + 1}`,
    };

    if (minute in specialCases) {
        return specialCases[minute];
    }

    return minute < 30
        ? `${minute} minutes past ${hour}`
        : `${60 - minute} minutes to ${hour + 1}`;
}


console.log(getSpokenTime(90, 0));
console.log(getSpokenTime(160, 120));
console.log(getSpokenTime(255, 180));
console.log(getSpokenTime(67.5, 92));
console.log(getSpokenTime(200, 240));
console.log(getSpokenTime(322.5, 273));
console.log(getSpokenTime(117.5, 335));
