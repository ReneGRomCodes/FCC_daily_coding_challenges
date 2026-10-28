/*
What Day Is It?
Given a Unix timestamp in milliseconds, return the day of the week.

Valid return days are:
"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"

Be sure to ignore time zones.

1. get_day_of_week(1775492249000) should return "Monday".
2. get_day_of_week(1766246400000) should return "Saturday".
3. get_day_of_week(33791256000000) should return "Tuesday".
4. get_day_of_week(1773576000000) should return "Sunday".
5. get_day_of_week(0) should return "Thursday".
 */

function getDayOfWeek(timestamp) {
    const days = {
        0: "Thursday",
        1: "Friday",
        2: "Saturday",
        3: "Sunday",
        4: "Monday",
        5: "Tuesday",
        6: "Wednesday",
    };
    const daysPassed = timestamp / 86_400_000;

    return days[Math.floor(daysPassed % 7)];
}


console.log(getDayOfWeek(1775492249000));
console.log(getDayOfWeek(1766246400000));
console.log(getDayOfWeek(33791256000000));
console.log(getDayOfWeek(1773576000000));
console.log(getDayOfWeek(0));
