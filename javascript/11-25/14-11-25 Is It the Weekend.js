/*
Is It the Weekend?
Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.

The weekend starts on Saturday.
If the given date is Saturday or Sunday, return "It's the weekend!".
Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
If X is 1, use "day" (singular) instead of "days" (plural).
Make sure the calculation ignores your local timezone.

1. days_until_weekend("2025-11-14") should return "1 day until the weekend.".
2. days_until_weekend("2025-01-01") should return "3 days until the weekend.".
3. days_until_weekend("2025-12-06") should return "It's the weekend!".
4. days_until_weekend("2026-01-27") should return "4 days until the weekend.".
5. days_until_weekend("2026-09-07") should return "5 days until the weekend.".
6. days_until_weekend("2026-11-29") should return "It's the weekend!".
 */

function daysUntilWeekend(dateString) {

    return dateString;
}


console.log(daysUntilWeekend("2025-11-14"));
console.log(daysUntilWeekend("2025-01-01"));
console.log(daysUntilWeekend("2025-12-06"));
console.log(daysUntilWeekend("2026-01-27"));
console.log(daysUntilWeekend("2026-09-07"));
console.log(daysUntilWeekend("2026-11-29"));
