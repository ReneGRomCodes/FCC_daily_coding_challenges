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

    return dateString;
}


console.log(getWeekday("2025-11-06"));
console.log(getWeekday("1999-12-31"));
console.log(getWeekday("1111-11-11"));
console.log(getWeekday("2112-12-21"));
console.log(getWeekday("2345-10-01"));
