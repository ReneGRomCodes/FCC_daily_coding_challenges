/*
Equinox Shadows

Today is the equinox, when the sun is directly above the equator and perfectly overhead at noon. Given a time, determine
the shadow cast by a 4-foot vertical pole.

- The time will be a string in "HH:MM" 24-hour format (for example, "15:00" is 3pm).
- You will only be given a time in 30 minute increments.

Rules:
- The sun rises at 6am directly "east", and sets at 6pm directly "west".
- A shadow always points opposite the sun.
- The shadow's length (in feet) is the number of hours away from noon, cubed.
- There is no shadow before sunrise (before 6am), after sunset (6pm or later), or at noon.

Return:
- If a shadow exists, return "(length)ft (direction)". For example, "8ft west".
- Otherwise, return "No shadow".

For example, given "10:00", return "8ft west" because 10am is 2 hours from noon, so 23 = 8 feet, and the shadow points
west because the sun is in the east at 10am.

1. get_shadow("10:00") should return "8ft west".
2. get_shadow("15:00") should return "27ft east".
3. get_shadow("12:00") should return "No shadow".
4. get_shadow("17:30") should return "166.375ft east".
5. get_shadow("05:00") should return "No shadow".
6. get_shadow("06:00") should return "216ft west".
7. get_shadow("18:00") should return "No shadow".
8. get_shadow("07:30") should return "91.125ft west".
9. get_shadow("00:00") should return "No shadow".
 */

function getShadow(time) {
    let hourDecimal = Number(time.slice(0, 2)) + time.slice(3) / 60;
    const isNight = hourDecimal < 6 || hourDecimal >= 18;
    const isNoon = hourDecimal === 12;

    if (isNight || isNoon) {
        return "No shadow";
    } else if (hourDecimal < 12) {
        return `${(12 - hourDecimal)**3}ft west`
    } else {
        return `${(hourDecimal - 12)**3}ft east`
    }
}


console.log(getShadow("10:00"));
console.log(getShadow("15:00"));
console.log(getShadow("12:00"));
console.log(getShadow("17:30"));
console.log(getShadow("05:00"));
console.log(getShadow("06:00"));
console.log(getShadow("18:00"));
console.log(getShadow("07:30"));
console.log(getShadow("00:00"));
