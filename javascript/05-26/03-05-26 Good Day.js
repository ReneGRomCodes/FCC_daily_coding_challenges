/*
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
 */

function getGreeting(time) {
    const morningStartHrs = 5 ;
    const afternoonStartHrs = 12;
    const eveningStartHrs = 18;
    const nightStartHrs = 22;
    const midnightMin = [0, 24 * 60];

    const [hrs, mins] = time.split(":").map(Number);
    const sMinutes = hrs * 60 + mins;

    const daytime = {
        "morning": [morningStartHrs * 60, afternoonStartHrs * 60],
        "afternoon": [afternoonStartHrs * 60, eveningStartHrs * 60],
        "evening": [eveningStartHrs * 60, nightStartHrs * 60],
        "night": [nightStartHrs * 60, midnightMin[1]],
        "NIGHT": [midnightMin[0], morningStartHrs * 60]
    };

    for (const [k, [start, end]] of Object.entries(daytime)) {
        if (sMinutes >= start && sMinutes < end) {
            return `Good ${k.toLowerCase()}`;
        }
    }
}


console.log(getGreeting("06:30"));
console.log(getGreeting("12:00"));
console.log(getGreeting("21:59"));
console.log(getGreeting("00:01"));
console.log(getGreeting("11:30"));
