/*
Speed Check
Given the speed you are traveling in miles per hour (MPH), and a speed limit in kilometers per hour (KPH), determine
whether you are speeding and if you will get a warning or a ticket.

1 mile equals 1.60934 kilometers.
If you are travelling less than or equal to the speed limit, return "Not Speeding".
If you are travelling 5 KPH or less over the speed limit, return "Warning".
If you are travelling more than 5 KPH over the speed limit, return "Ticket".

1. speed_check(30, 70) should return "Not Speeding".
2. speed_check(40, 60) should return "Warning".
3. speed_check(40, 65) should return "Not Speeding".
4. speed_check(60, 90) should return "Ticket".
5. speed_check(65, 100) should return "Warning".
6. speed_check(88, 40) should return "Ticket".
 */

function speedCheck(speedMph, speedLimitKph) {
    const speedKph = speedMph * 1.60934;

    if (speedKph <= speedLimitKph) { return "Not Speeding" }
    else if (speedKph <= speedLimitKph + 5) { return "Warning" }
    else { return "Ticket" }
}

// Cursed and borderline unreadable version using a nested ternary operator in an arrow function... just for shits and giggles.
const cursedSpeedCheck = (s, l) => s * 1.60934 <= l ? "Not Speeding" : s * 1.60934 <= l + 5 ? "Warning" : "Ticket";


console.log(speedCheck(30, 70));
console.log(speedCheck(40, 60));
console.log(speedCheck(40, 65));
console.log(speedCheck(60, 90));
console.log(speedCheck(65, 100));
console.log(speedCheck(88, 40));
