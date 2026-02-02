/*
Digital Detox
Given an array of your login logs, determine whether you have met your digital detox goal.

Each log is a string in the format "YYYY-MM-DD HH:mm:ss".

You have met your digital detox goal if both of the following statements are true:

You logged in no more than once within any four-hour period.
You logged in no more than 2 times on any single day.

1. digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]) should return True.
2. digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"]) should return False.
3. digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"])
    should return True.
4. digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"])
    should return False.
5. digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00",
    "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"])
    should return True.
6. digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00",
    "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"])
    should return False.
 */

function digitalDetox(logs) {
    if (logs.length < 2) return true;

    // Rule 2: no more than 2 logins per day.
    const perDay = Object.create(null);

    for (const log of logs) {
        const day = log.slice(0, 10);
        perDay[day] = (perDay[day] ?? 0) + 1;
        if (perDay[day] > 2) return false;
    }

    // Rule 1: no more than once in any 4-hour window.
    logs.sort();  // ISO timestamps sort chronologically as strings.

    const toMinutes = (time) =>
        Number(time.slice(0, 2)) * 60 + Number(time.slice(3, 5));

    let prevDay = logs[0].slice(0, 10);
    let prevMin = toMinutes(logs[0].slice(11));

    for (let i = 1; i < logs.length; i++) {
        const log = logs[i];
        const day = log.slice(0, 10);
        const curMin = toMinutes(log.slice(11));

        const diff =
            day === prevDay
                ? curMin - prevMin
                : curMin + 1440 - prevMin;  // Crossed midnight.

        if (diff < 240) return false;

        prevDay = day;
        prevMin = curMin;
    }

    return true;
}


console.log(digitalDetox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]));
console.log(digitalDetox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"]));
console.log(digitalDetox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"]));
console.log(digitalDetox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"]));
console.log(digitalDetox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00",
    "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]));
console.log(digitalDetox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00",
    "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]));
