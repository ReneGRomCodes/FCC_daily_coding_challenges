/*
Birthday Countdown
Given today's date and a birthday, return the number of days until the person's next birthday.

- Today's date is given as a string in "YYYY-MM-DD" format, with leading zeros, for example: "2026-07-16".
- The birthday is given as a string in "M/D" format, without leading zeros, for example: "9/7".
- If today is their birthday, return the number of days until their next birthday (not 0).
- Leap years should be accounted for.

1. days_until_birthday("2026-07-16", "9/7") should return 53.
2. days_until_birthday("2026-07-16", "3/22") should return 249.
3. days_until_birthday("2026-07-16", "7/16") should return 365.
4. days_until_birthday("2024-02-28", "3/1") should return 2.
5. days_until_birthday("2023-04-24", "12/30") should return 250.
6. days_until_birthday("2024-03-01", "2/29") should return 1460.
7. days_until_birthday("2096-03-01", "2/29") should return 2920.
 */

function daysUntilBirthday(today, birthday) {
    const [year, month, day] = today.split('-').map(Number);
    const todayDate = new Date(Date.UTC(year, month - 1, day)); // JS months are 0-indexed
    const [bMonth, bDay] = birthday.split('/').map(Number);
    let targetYear = todayDate.getUTCFullYear();

    while (true) {
        const candidate = new Date(Date.UTC(targetYear, bMonth - 1, bDay));
        const isValidDate = candidate.getUTCMonth() === (bMonth - 1);

        if (isValidDate && candidate > todayDate) {
            const msPerDay = 1000 * 60 * 60 * 24;
            return Math.round((candidate - todayDate) / msPerDay);
        }

        targetYear++;
    }
}


console.log(daysUntilBirthday("2026-07-16", "9/7"));
console.log(daysUntilBirthday("2026-07-16", "3/22"));
console.log(daysUntilBirthday("2026-07-16", "7/16"));
console.log(daysUntilBirthday("2024-02-28", "3/1"));
console.log(daysUntilBirthday("2023-04-24", "12/30"));
console.log(daysUntilBirthday("2024-03-01", "2/29"));
console.log(daysUntilBirthday("2096-03-01", "2/29"));
