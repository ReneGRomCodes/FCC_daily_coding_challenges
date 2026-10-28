/*
Rental Cost
Given a rental timestamp, a return timestamp, and a rental tier, return the total cost of the rental including any late
fees.

- Given timestamps are UTC ISO strings, for example: "2026-06-18T18:30:00Z".
- The rental tier is the number of days before the rental is due back: 1, 3, or 7.
- Rentals are due back by 12:00 PM UTC or earlier on the last day of the rental period. For example, a 1-day rental checked
  out at any time on March 15 is due back by 12:00 PM UTC on March 16.
- Each day past the due date and time incurs a late fee.

Pricing is as follows:
Tier	Base cost	Late fee per day
1 day	$4.99	    $3.99
3 days	$3.99	    $2.99
7 days	$2.99	    $0.99

Return the total cost rounded to two decimal places in the format "$D.CC".

1. get_rental_cost("2026-06-18T18:30:00Z", "2026-06-19T10:30:00Z", 1) should return "$4.99".
2. get_rental_cost("2026-06-18T14:30:00Z", "2026-06-20T12:30:00Z", 1) should return "$12.97".
3. get_rental_cost("2026-06-18T10:15:00Z", "2026-06-18T19:45:00Z", 3) should return "$3.99".
4. get_rental_cost("2026-06-18T15:20:00Z", "2026-06-23T08:10:00Z", 3) should return "$9.97".
5. get_rental_cost("2026-06-18T12:00:00Z", "2026-06-25T12:00:00Z", 7) should return "$2.99".
6. get_rental_cost("2026-06-18T08:00:00Z", "2027-06-18T14:00:00Z", 7) should return "$358.40".
 */

const PRICING = {
    1: { base: 4.99, lateFee: 3.99 },
    3: { base: 3.99, lateFee: 2.99 },
    7: { base: 2.99, lateFee: 0.99 },
};

// Parses "YYYY-MM-DDTHH:MM:SSZ" into its numeric parts.
function parseTimestamp(ts) {
    const [datePart, timePart] = ts.slice(0, -1).split("T"); // drop trailing "Z".
    const [year, month, day] = datePart.split("-").map(Number);
    const [hour, minute, second] = timePart.split(":").map(Number);
    return { year, month, day, hour, minute, second };
}

// Converts a calendar date to a day number (proleptic Gregorian), no Date object needed.
function daysSinceEpoch(year, month, day) {
    const a = Math.floor((14 - month) / 12);
    const y = year + 4800 - a;
    const m = month + 12 * a - 3;
    return (
        day +
        Math.floor((153 * m + 2) / 5) +
        365 * y +
        Math.floor(y / 4) -
        Math.floor(y / 100) +
        Math.floor(y / 400)
    );
}

function getRentalCost(rented, returned, tier) {
    const { base, lateFee } = PRICING[tier];

    const r = parseTimestamp(rented);
    const ret = parseTimestamp(returned);

    const rentedDayNum = daysSinceEpoch(r.year, r.month, r.day);
    const returnedDayNum = daysSinceEpoch(ret.year, ret.month, ret.day);

    const dueDayNum = rentedDayNum + tier;
    const dueHour = 12;

    let lateDays;
    const isLate =
        returnedDayNum > dueDayNum ||
        (returnedDayNum === dueDayNum &&
            (ret.hour > dueHour ||
                (ret.hour === dueHour && (ret.minute > 0 || ret.second > 0))));

    if (!isLate) {
        lateDays = 0;
    } else if (returnedDayNum === dueDayNum) {
        // late on the due day itself (after 12:00) -> 1 late day.
        lateDays = 1;
    } else {
        const dayDiff = returnedDayNum - dueDayNum;
        const returnedAtOrBeforeNoon =
            ret.hour < dueHour || (ret.hour === dueHour && ret.minute === 0 && ret.second === 0);
        lateDays = returnedAtOrBeforeNoon ? dayDiff : dayDiff + 1;
    }

    const total = base + lateDays * lateFee;
    return `$${total.toFixed(2)}`;
}


console.log(getRentalCost("2026-06-18T18:30:00Z", "2026-06-19T10:30:00Z", 1));
console.log(getRentalCost("2026-06-18T14:30:00Z", "2026-06-20T12:30:00Z", 1));
console.log(getRentalCost("2026-06-18T10:15:00Z", "2026-06-18T19:45:00Z", 3));
console.log(getRentalCost("2026-06-18T15:20:00Z", "2026-06-23T08:10:00Z", 3));
console.log(getRentalCost("2026-06-18T12:00:00Z", "2026-06-25T12:00:00Z", 7));
console.log(getRentalCost("2026-06-18T08:00:00Z", "2027-06-18T14:00:00Z", 7));
