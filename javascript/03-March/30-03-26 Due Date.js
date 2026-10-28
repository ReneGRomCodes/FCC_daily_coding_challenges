/*
Due Date
Given a date string, return the date 9 months in the future.

- The given and return strings have the format "YYYY-MM-DD".
- If the month nine months into the future doesn't contain the original day number, return the last day of that month.

1. get_due_date("2025-03-30") should return "2025-12-30".
2. get_due_date("2025-04-27") should return "2026-01-27".
3. get_due_date("2025-05-29") should return "2026-02-28".
4. get_due_date("2026-06-30") should return "2027-03-30".
5. get_due_date("2026-10-11") should return "2027-07-11".
 */

function getDueDate(dateStr) {
    const monthLengths = {
        30: [4, 6, 9, 11],
        31: [1, 3, 5, 7, 8, 10, 12],
        28: [2]
    };

    let [year, month, day] = dateStr.split('-').map(Number);

    month += 9;
    if (month > 12) {
        year += 1;
        month -= 12;
    }

    for (const [length, months] of Object.entries(monthLengths)) {
        if (months.includes(month) && day > Number(length)) {
            day = Number(length);
        }
    }

    return `${year}-${String(month).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
}


console.log(getDueDate("2025-03-30"));
console.log(getDueDate("2025-04-27"));
console.log(getDueDate("2025-05-29"));
console.log(getDueDate("2026-06-30"));
console.log(getDueDate("2026-10-11"));
