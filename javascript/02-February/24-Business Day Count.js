/*
Business Day Count
Given a start date and an end date, return the number of business days between the two.

Given dates are in the format "YYYY-MM-DD".
Weekdays are business days (Monday through Friday).
Weekends are not business days (Saturday and Sunday).
Include both the start and end dates when counting.

1. count_business_days("2026-02-24", "2026-02-26") should return 3.
2. count_business_days("2026-02-24", "2026-02-28") should return 4.
3. count_business_days("2026-02-21", "2026-03-01") should return 5.
4. count_business_days("2026-03-08", "2026-03-17") should return 7.
5. count_business_days("2026-02-24", "2027-02-24") should return 262.
 */

function countBusinessDays(startDate, endDate) {
    const start = new Date(startDate);
    const end = new Date(endDate);

    let count = 0;
    let current = new Date(start);

    while (current <= end) {
        const day = current.getDay(); // 0 = Sunday, 6 = Saturday

        if (day !== 0 && day !== 6) {
            count++;
        }

        current.setDate(current.getDate() + 1);
    }

    return count;
}


console.log(countBusinessDays("2026-02-24", "2026-02-26"));
console.log(countBusinessDays("2026-02-24", "2026-02-28"));
console.log(countBusinessDays("2026-02-21", "2026-03-01"));
console.log(countBusinessDays("2026-03-08", "2026-03-17"));
console.log(countBusinessDays("2026-02-24", "2027-02-24"));
