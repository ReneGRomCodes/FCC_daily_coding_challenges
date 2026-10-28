/*
Closest Time Direction
Given two times, determine whether you can get from the first to the second faster by moving forward or backward.

- Times are given in 24-hour format ("HH:MM")
- The clock wraps around (23:59 goes to 00:00 when moving forward, and 00:00 goes to 23:59 when moving backwards)

Return:
- "forward" if moving forward is shorter
- "backward" if moving backward is shorter
- "equal" if both directions take the same amount of time

1. get_direction("10:00", "12:00") should return "forward".
2. get_direction("11:00", "05:00") should return "backward".
3. get_direction("00:00", "12:00") should return "equal".
4. get_direction("15:45", "01:10") should return "forward".
5. get_direction("03:30", "19:50") should return "backward".
6. get_direction("06:30", "18:30") should return "equal".
 */

function getDirection(time1, time2) {
    const toMinutes = (t) => {
        const [h, m] = t.split(":").map(Number);
        return h * 60 + m;
    };

    const m1 = toMinutes(time1);
    const m2 = toMinutes(time2);

    const diff = (m2 - m1 + 1440) % 1440;

    if (diff < 720) return "forward";
    if (diff > 720) return "backward";
    return "equal";
}


console.log(getDirection("10:00", "12:00"));
console.log(getDirection("11:00", "05:00"));
console.log(getDirection("00:00", "12:00"));
console.log(getDirection("15:45", "01:10"));
console.log(getDirection("03:30", "19:50"));
console.log(getDirection("06:30", "18:30"));
