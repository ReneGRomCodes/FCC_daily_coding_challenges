/*
Weekday Finder
Given a string date in the format YYYY-MM-DD, return the day of the week.

Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.

1. get_weekday("2025-11-06") should return Thursday.
2. get_weekday("1999-12-31") should return Friday.
3. get_weekday("1111-11-11") should return Saturday.
4. get_weekday("2112-12-21") should return Wednesday.
5. get_weekday("2345-10-01") should return Monday.
 */

function getWeekday(dateString) {
    // Find and return weekday for given date string using Zeller's Congruence.
    let [year, month, day] = dateString.split("-").map(Number);
    const weekdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];

    if (month < 3) {
        month += 12;
        year--;
    }

    const yearpart = year % 100;
    const century = Math.floor(year / 100);

    const dayIndex = (day + Math.floor((13 * (month + 1)) / 5) + yearpart + Math.floor(yearpart / 4) + Math.floor(century / 4) + 5 * century) % 7;

    return weekdays[dayIndex];
}


console.log(getWeekday("2025-11-06"));
console.log(getWeekday("1999-12-31"));
console.log(getWeekday("1111-11-11"));
console.log(getWeekday("2112-12-21"));
console.log(getWeekday("2345-10-01"));
