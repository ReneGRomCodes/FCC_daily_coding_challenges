/*
Space Week Day 6: Moon Phase
For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the
moon for that day using the following rules:

Use a simplified lunar cycle of 28 days, divided into four equal phases:

"New": days 1 - 7
"Waxing": days 8 - 14
"Full": days 15 - 21
"Waning": days 22 - 28
After day 28, the cycle repeats with day 1, a new moon.

Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
You will not be given any dates before the reference date.
Return the correct phase as a string.

1. moon_phase("2000-01-12") should return "New".
2. moon_phase("2000-01-13") should return "Waxing".
3. moon_phase("2014-10-15") should return "Full".
4. moon_phase("2012-10-21") should return "Waning".
5. moon_phase("2022-12-14") should return "New".
 */

function moonPhase(dateString) {
    const date = new Date(`${dateString}T00:00:00Z`);
    const reference = new Date("2000-01-06T00:00:00Z");

    const daysSince = Math.floor((date - reference) / (1000 * 60 * 60 * 24));
    const dayInCycle = daysSince % 28;

    if (dayInCycle <= 6) {
        return "New";
    } else if (dayInCycle <= 13) {
        return "Waxing";
    } else if (dayInCycle <= 20) {
        return "Full";
    } else {
        return "Waning";
    }
}


console.log(moonPhase("2000-01-12"));
console.log(moonPhase("2000-01-13"));
console.log(moonPhase("2014-10-15"));
console.log(moonPhase("2012-10-21"));
console.log(moonPhase("2022-12-14"));
